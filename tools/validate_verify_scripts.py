#!/usr/bin/env python3
"""
Worksheet Verification Scripts Validator.
This script checks that all sheetNN_verify.py scripts in algebra/verify/ and combinatorics/verify/
conform to speed-maths project requirements:
1. Run without -O flag exits with code 0.
2. Run with -O flag exits with code 2.
3. Contains optimization guard in main().
4. Contains CHECKS dictionary.
5. Defines all 33 standard check functions (A1-A10, B1-B10, C1-C8, D1-D5).
6. Each check function has a docstring specifying either 'EXHAUSTIVE PROOF' or 'SAMPLED CHECK'.
"""

import os
import sys
import glob
import ast
import subprocess

def get_expected_labels():
    expected = []
    for letter, count in [('A', 10), ('B', 10), ('C', 8), ('D', 5)]:
        for i in range(1, count + 1):
            expected.append(f"{letter}{i}")
    return expected

def validate_script(script_path):
    rel_path = os.path.relpath(script_path)
    print(f"Validating {rel_path}...")
    errors = []
    
    # 1. Run without -O flag
    try:
        res = subprocess.run([sys.executable, script_path], capture_output=True, text=True, timeout=60)
        if res.returncode != 0:
            errors.append(
                f"Execution without -O failed (exit code {res.returncode}).\n"
                f"--- stdout ---\n{res.stdout}\n"
                f"--- stderr ---\n{res.stderr}\n"
            )
    except subprocess.TimeoutExpired:
        errors.append("Execution without -O timed out after 60 seconds.")
    except Exception as e:
        errors.append(f"Failed to execute without -O: {e}")

    # 2. Run with -O flag
    try:
        res_o = subprocess.run([sys.executable, "-O", script_path], capture_output=True, text=True, timeout=60)
        if res_o.returncode != 2:
            errors.append(
                f"Execution with -O did not exit with code 2 (exit code {res_o.returncode}).\n"
                f"--- stdout ---\n{res_o.stdout}\n"
                f"--- stderr ---\n{res_o.stderr}\n"
            )
    except subprocess.TimeoutExpired:
        errors.append("Execution with -O timed out after 60 seconds.")
    except Exception as e:
        errors.append(f"Failed to execute with -O: {e}")

    # 3. Read and parse AST
    try:
        with open(script_path, "r", encoding="utf-8") as f:
            content = f.read()
        tree = ast.parse(content)
    except Exception as e:
        errors.append(f"Failed to parse source file with AST: {e}")
        # If parsing fails, we cannot run AST checks
        print(f"  RESULT: FAIL (AST parsing error)\n")
        return False, errors

    # Check for main() and debug guard
    main_node = None
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "main":
            main_node = node
            break

    if not main_node:
        errors.append("Function 'main()' is not defined.")
    else:
        has_guard = False
        for child in ast.walk(main_node):
            if isinstance(child, ast.If):
                test = child.test
                if (isinstance(test, ast.UnaryOp) and 
                    isinstance(test.op, ast.Not) and 
                    isinstance(test.operand, ast.Name) and 
                    test.operand.id == '__debug__'):
                    has_guard = True
                    break
        if not has_guard:
            errors.append("Function 'main()' is missing the optimization guard: 'if not __debug__:'")

    # Check for CHECKS dictionary
    checks_dict = None
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == 'CHECKS':
                    if isinstance(node.value, ast.Dict):
                        checks_dict = {}
                        for k, v in zip(node.value.keys, node.value.values):
                            key = None
                            if isinstance(k, ast.Constant):
                                key = k.value
                            elif isinstance(k, ast.Str):
                                key = k.s
                            
                            val_name = None
                            if isinstance(v, ast.Name):
                                val_name = v.id
                            elif isinstance(v, ast.Attribute):
                                val_name = v.attr
                            
                            if key is not None and val_name is not None:
                                checks_dict[key] = val_name
                        break
            if checks_dict is not None:
                break

    if checks_dict is None:
        errors.append("Dictionary 'CHECKS' is not defined at the module level.")

    # Check defined functions and docstrings
    defined_functions = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            defined_functions[node.name] = node

    expected_labels = get_expected_labels()
    missing_funcs = []
    missing_checks_mapping = []
    bad_docstrings = []

    for label in expected_labels:
        func_name = f"check_{label}"
        if func_name not in defined_functions:
            missing_funcs.append(func_name)
            continue
        
        func_node = defined_functions[func_name]
        doc = ast.get_docstring(func_node)
        if not doc:
            bad_docstrings.append(f"{func_name} is missing a docstring.")
        else:
            doc_upper = doc.upper()
            if "EXHAUSTIVE PROOF" not in doc_upper and "SAMPLED CHECK" not in doc_upper:
                bad_docstrings.append(
                    f"{func_name} docstring does not contain either 'EXHAUSTIVE PROOF' or 'SAMPLED CHECK'. "
                    f"Got: {repr(doc)}"
                )

        if checks_dict is not None:
            if label not in checks_dict:
                missing_checks_mapping.append(f"Label {repr(label)} not mapped in CHECKS.")
            elif checks_dict[label] != func_name:
                missing_checks_mapping.append(
                    f"Label {repr(label)} is mapped to {repr(checks_dict[label])} instead of {repr(func_name)}."
                )

    if missing_funcs:
        errors.append(f"Missing expected check function definitions: {', '.join(missing_funcs)}")
    if missing_checks_mapping:
        errors.append(f"CHECKS dictionary mapping issues: {', '.join(missing_checks_mapping)}")
    if bad_docstrings:
        errors.append("Check function docstring violations:")
        for msg in bad_docstrings:
            errors.append(f"  - {msg}")

    if errors:
        print("  RESULT: FAIL")
        for err in errors:
            print(f"    * {err}")
        print()
        return False, errors
    else:
        print("  RESULT: PASS\n")
        return True, []

def main():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    search_patterns = [
        os.path.join(project_root, "algebra", "verify", "sheet[0-9][0-9]_verify.py"),
        os.path.join(project_root, "combinatorics", "verify", "sheet[0-9][0-9]_verify.py")
    ]
    
    scripts = []
    for pattern in search_patterns:
        scripts.extend(glob.glob(pattern))
    scripts = sorted(list(set(scripts)))
    
    if not scripts:
        print("Error: No worksheet verification scripts found.")
        sys.exit(1)
        
    print(f"Found {len(scripts)} verification script(s) to validate.")
    all_pass = True
    results = {}
    
    for script in scripts:
        success, errors = validate_script(script)
        results[script] = (success, errors)
        if not success:
            all_pass = False
            
    if all_pass:
        print("All verification scripts validated successfully!")
        sys.exit(0)
    else:
        print("Some verification scripts failed validation.")
        sys.exit(1)

if __name__ == "__main__":
    main()
