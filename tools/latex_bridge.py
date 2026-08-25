import os
import re
import sympy
from sympy.parsing.latex import parse_latex

def extract_tex_answers(tex_path):
    answers = {}
    if not os.path.exists(tex_path):
        return answers
        
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Speed Maths headers look like: %── A1 ───────────────────
    sections = re.finditer(r'%[─=]+\s*([A-D][0-9]+)\s*[─=]+', content)
    sec_pos = [(m.group(1), m.start()) for m in sections]
    
    ans_matches = list(re.finditer(r'\\ans\{(.*)\}', content))
    
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
            answers[closest_sec] = ans_text.strip()

    if len(answers) < len(ans_matches):
        sec_headings = list(re.finditer(r'\\section\*\{Section\s*([A-D])', content))
        if sec_headings:
            for i, sh in enumerate(sec_headings):
                sec_letter = sh.group(1)
                start_pos = sh.start()
                end_pos = sec_headings[i+1].start() if i+1 < len(sec_headings) else len(content)
                sec_content = content[start_pos:end_pos]
                sec_ans = list(re.finditer(r'\\ans\{(.*)\}', sec_content))
                for q_idx, am in enumerate(sec_ans, start=1):
                    key = f"{sec_letter}{q_idx}"
                    if key not in answers:
                        answers[key] = am.group(1).strip()
            
    return answers

def parse_tex_math(tex_str):
    """
    Cleans up common LaTeX formatting from the \ans{} macro and parses to SymPy.
    """
    # Remove $ signs
    tex_str = tex_str.replace('$', '').strip()
    # Handle True/False text
    clean_lower = tex_str.strip().lower()
    if clean_lower.startswith('true'):
        return True
    if clean_lower.startswith('false'):
        return False

    # Handle single option letters like A, B, C, D, E
    if tex_str.strip() in ('A', 'B', 'C', 'D', 'E'):
        return tex_str.strip()

    # Quoted prose answers
    if '"' in tex_str or '``' in tex_str or "''" in tex_str:
        return tex_str.strip()

    # Strip leading descriptive prefixes before prose detection
    tex_str = re.sub(r'^\s*(?:Both count|Both are|The odd ones are exactly|Row\s+[0-9]+:?|Case\s+[0-9]+:?)\s*', '', tex_str, flags=re.IGNORECASE)

    # Check if predominantly English descriptive text
    english_words = [
        r'proof', r'proofs', r'proved', r'counterexample', r'no\s+solution', r'all\s+integers',
        r'all\s+real', r'all\s+sign\s+combinations', r'divisible', r'smallest', r'minimum', r'maximum',
        r'under', r'see\s+method', r'equality\s+iff', r'remainder\s+at', r'composite',
        r'continuity', r'non-negative', r'impossible', r'decreasing', r'increasing', r'odd', r'even',
        r'not\s+necessarily', r'error', r'fractions', r'sequence', r'bounded', r'convergent',
        r'for\s+all', r'for\s+any', r'for\s+any\s+constant', r'gives', r'maximum\s+is', r'minimum\s+is',
        r'forced', r'contradiction', r'someone', r'pigeonhole', r'some\s+three',
        r'affirming', r'denying', r'consequent', r'antecedent', r'sufficient',
        r'necessary', r'neither', r'inductive', r'induction', r'base\s+case',
        r'suppose', r'assume', r'exists', r'every', r'there\s+exists',
        r'tautology', r'fallacy', r'line\s+[0-9]+', r'circular\s+reasoning', r'negation',
        r'converse', r'inverse', r'contrapositive', r'must', r'sound', r'valid', r'invalid', r'truth',
        r'true', r'false', r'prime', r'primes', r'squarefree', r'product', r'distinct',
        r'no', r'yes', r'i\s+and\s+iii', r'ii\s+and\s+iii', r'i\s+and\s+ii', r'i\s+only', r'ii\s+only', r'iii\s+only',
        r'arbitrary', r'fixed', r'for\s+some', r'never', r'derived', r'chain', r'starts', r'implications'
    ]
    english_pattern = re.compile(r'\b(?:' + '|'.join(english_words) + r')\b', re.IGNORECASE)
    if english_pattern.search(tex_str):
        return tex_str.strip()

    # Clean formatting
    cleaned = tex_str.replace('{,}', '').replace(r'\,', ' ').replace(r'\;', ' ').replace(r'\ ', ' ').replace('~', ' ')
    cleaned = re.sub(r';\s*undefined\s+at\s+.*', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\\(?:quad|qquad|displaystyle|left|right|checkmark)\b', ' ', cleaned)
    cleaned = re.sub(r'\\text\{([^}]*)\}', r' \1 ', cleaned)
    cleaned = re.sub(r'\\sqrt(?![{\[])([0-9a-zA-Z]+)', r'\\sqrt{\1}', cleaned)
    cleaned = re.sub(r'\\dfrac\b', r'\\frac', cleaned)
    cleaned = re.sub(r'\\tfrac\b', r'\\frac', cleaned)
    cleaned = cleaned.strip()
    
    def _clean_functions(e):
        if not isinstance(e, sympy.Basic):
            return e
        for func in list(e.atoms(sympy.core.function.AppliedUndef)):
            fname = func.__class__.__name__
            if len(fname) == 1 and fname.isalpha():
                sym = sympy.Symbol(fname)
                e = e.replace(func.__class__, lambda *args: sym * sympy.Mul(*args))
        return e

    # Strip parenthetical annotations like (all four real) or (double) or (one real solution)
    cleaned = re.sub(r'\([^)]*(?:real|double|root|equiv|giving|solution|multiplicity|or\s+|any\s+|for\s+any|lines?)[^)]*\)', '', cleaned)
    cleaned = re.sub(r'\b(?:only|giving|always)\b', '', cleaned)
    cleaned = re.sub(r'\b(?:Row\s+[0-9]+|Case\s+[0-9]+):?\s*', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\b(?:Both count|Both are|The odd ones are exactly|at least|at most|each team plays\s+[0-9]+|each team plays)\b', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\b(?:segments?|triangles?|in total|total|avoid(?:ing)?(?:\s+[a-zA-Z])?|ways|matches|teams?|students?|points?|digits?|cards?|rectangles?|squares?|paths?|subsets?|people|hands?|which is [0-9]+)\b', ' ', cleaned, flags=re.IGNORECASE)
    cleaned = cleaned.strip().rstrip('.')

    def _split_top_level(text, delims=(',', ';')):
        parts = []
        current = []
        depth = 0
        for char in text:
            if char in '{[(':
                depth += 1
                current.append(char)
            elif char in '}])':
                depth = max(0, depth - 1)
                current.append(char)
            elif depth == 0 and char in delims:
                parts.append(''.join(current).strip())
                current = []
            else:
                current.append(char)
        if current:
            parts.append(''.join(current).strip())
        return [p for p in parts if p]

    # If chained equality like r = 1 - a/S = (S-a)/S
    if ';' not in cleaned and ',' not in cleaned and ' and ' not in cleaned and ' or ' not in cleaned:
        parts = _split_top_level(cleaned, ('=',))
        if len(parts) >= 3:
            try:
                expr = parse_latex(parts[-1])
                return _clean_functions(expr)
            except Exception:
                pass

    # Handle semicolon separated multi-part answers
    if ';' in cleaned:
        parts = _split_top_level(cleaned, (';',))
        if len(parts) > 1:
            try:
                parsed_parts = [parse_tex_math(p) for p in parts]
                return parsed_parts
            except Exception:
                pass

    # Handle and/or separated equations or values like x=5 or x=-2
    if ' or ' in cleaned or ' and ' in cleaned:
        parts = [p.strip() for p in re.split(r'\s+(?:and|or)\s+', cleaned) if p.strip()]
        if len(parts) > 1:
            try:
                parsed_parts = [parse_tex_math(p) for p in parts]
                return parsed_parts
            except Exception:
                pass

    # Handle top-level comma-separated lists like 1, 5, 10, 10, 5, 1 or a=-12, b=16
    if ',' in cleaned and not (cleaned.startswith('{') and cleaned.endswith('}')) and not (cleaned.startswith('(') and cleaned.endswith(')')):
        parts = _split_top_level(cleaned, (',',))
        if len(parts) > 1:
            expanded_parts = []
            for p in parts:
                if r'\pm' in p:
                    expanded_parts.append(p.replace(r'\pm', '+'))
                    expanded_parts.append(p.replace(r'\pm', '-'))
                else:
                    expanded_parts.append(p)
            try:
                parsed_parts = [parse_tex_math(p) for p in expanded_parts]
                if all(not isinstance(p, str) for p in parsed_parts):
                    return parsed_parts
            except Exception:
                pass

    try:
        expr = parse_latex(cleaned)
        if isinstance(expr, (bool, sympy.logic.boolalg.BooleanAtom)) and not cleaned.lower().startswith(('true', 'false')) and '=' in cleaned:
            parts = [p.strip() for p in cleaned.split('=')]
            try:
                expr = parse_latex(parts[-1])
            except Exception:
                pass
        return _clean_functions(expr)
    except Exception as e:
        try:
            expr = parse_latex(tex_str)
            if isinstance(expr, (bool, sympy.logic.boolalg.BooleanAtom)) and not tex_str.lower().startswith(('true', 'false')) and '=' in tex_str:
                parts = [p.strip() for p in tex_str.split('=')]
                try:
                    expr = parse_latex(parts[-1])
                except Exception:
                    pass
            return _clean_functions(expr)
        except Exception:
            return tex_str

def get_answer(tex_path, label):
    answers = extract_tex_answers(tex_path)
    if label not in answers:
        raise ValueError(f"Label {label} not found in {tex_path}")
    
    raw_tex = answers[label]
    return parse_tex_math(raw_tex)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        tex_path = sys.argv[1]
        print(f"Answers in {tex_path}:")
        answers = extract_tex_answers(tex_path)
        for label, raw_tex in answers.items():
            parsed = parse_tex_math(raw_tex)
            print(f" {label}: {raw_tex} -> SymPy: {parsed} (type: {type(parsed)})")
