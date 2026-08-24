import os
import re
import glob

def get_tex_answers(tex_file):
    answers = {}
    if not os.path.exists(tex_file): return answers
    with open(tex_file, 'r') as f:
        content = f.read()
    
    sections = re.finditer(r'%[─=]+\s*([A-D][0-9]+)\s*[─=]+', content)
    sec_pos = [(m.group(1), m.start()) for m in sections]
    
    ans_matches = list(re.finditer(r'\\ans\{([^}]*)\}', content))
    
    for m in ans_matches:
        pos = m.start()
        ans_text = m.group(1)
        closest_sec = None
        for sec, spos in sec_pos:
            if spos < pos:
                closest_sec = sec
            else:
                break
        if closest_sec:
            answers[closest_sec] = ans_text
    return answers

def get_py_checks(py_file):
    checks = {}
    if not os.path.exists(py_file): return checks
    with open(py_file, 'r') as f:
        content = f.read()
    
    matches = re.finditer(r'def (check_[A-D][0-9]+)\(\):', content)
    starts = [(m.group(1), m.start()) for m in matches]
    
    for i, (name, pos) in enumerate(starts):
        end_pos = starts[i+1][1] if i+1 < len(starts) else len(content)
        checks[name] = content[pos:end_pos].strip()
    return checks

def check_facade(func_str):
    if "assert True" in func_str: return "assert True"
    
    asserts = re.findall(r'assert\s+(.*)', func_str)
    for a in asserts:
        if '==' in a:
            left, right = a.split('==', 1)
            # Remove comments
            right = right.split('#')[0]
            if left.strip() == right.strip():
                return f"Tautology: {a}"
    
    trivial_math = re.findall(r'assert\s+\d+\s*[\*\+\-\/]\s*\d+\s*==\s*\d+', func_str)
    if trivial_math:
        return f"Trivial Math: {trivial_math[0]}"
        
    # Check for empty checks (no assertions)
    if not asserts:
        return "No assertions found"

    return False

pillars = ['combinatorics', 'algebra', 'logic', 'number-theory']
for pillar in pillars:
    for i in range(7, 0, -1):
        num = f"{i:02d}"
        tex_file = f"{pillar}/answers/ans{num}.tex"
        py_file = f"{pillar}/verify/sheet{num}_verify.py"
        
        if not os.path.exists(tex_file) or not os.path.exists(py_file):
            continue
            
        tex_answers = get_tex_answers(tex_file)
        py_checks = get_py_checks(py_file)
        
        facades = []
        for q, func in py_checks.items():
            qid = q.replace('check_', '')
            is_facade = check_facade(func)
            if is_facade:
                facades.append((qid, is_facade))
        
        if facades:
            print(f"\n[{pillar} sheet {num}] Found {len(facades)} facade checks:")
            for q, reason in facades:
                print(f"  {q}: {reason}")
