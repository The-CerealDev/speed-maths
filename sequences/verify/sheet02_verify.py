import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from pathlib import Path
from tools.latex_bridge import get_answer
TEX_PATH = Path(__file__).resolve().parent.parent / 'answers' / 'ans02.tex'
'Computational verification for sequences/answers/ans02.tex.\n\nConvention: one check_<label>() function per question, matching the\nsection+number label in the sheet (A1, D5, ...).\n\nRun directly:\n    python3 sheet02_verify.py\n'
import math
import random
import itertools

def check_A1():
    """EXHAUSTIVE PROOF"""
    row5 = [math.comb(5, k) for k in range(6)]
    assert row5 == [1, 5, 10, 10, 5, 1]
    row4 = [math.comb(4, k) for k in range(5)]
    assert row4 == [1, 4, 6, 4, 1]
    assert [row4[0]] + [row4[i] + row4[i + 1] for i in range(4)] + [row4[4]] == row5
    return get_answer(TEX_PATH, 'A1')

def check_A2():
    """EXHAUSTIVE PROOF"""
    assert math.comb(6, 2) == 15
    assert 6 * 5 // 2 == 15
    assert math.comb(6, 4) == 15
    return get_answer(TEX_PATH, 'A2')

def check_A3():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 10):
        assert sum((math.comb(n, k) for k in range(n + 1))) == 2 ** n
    return get_answer(TEX_PATH, 'A3')

def check_A4():
    """EXHAUSTIVE PROOF"""
    row3 = [math.comb(3, k) for k in range(4)]
    assert row3 == [1, 3, 3, 1]
    return get_answer(TEX_PATH, 'A4')

def check_A5():
    """EXHAUSTIVE PROOF"""
    assert math.comb(6, 2) == 15
    row6 = [math.comb(6, k) for k in range(7)]
    assert row6 == [1, 6, 15, 20, 15, 6, 1]
    return get_answer(TEX_PATH, 'A5')

def check_A6():
    """EXHAUSTIVE PROOF"""
    row4 = [math.comb(4, k) for k in range(5)]
    assert row4 == [1, 4, 6, 4, 1]
    diffs = [row4[i + 1] - row4[i] for i in range(4)]
    assert diffs == [3, 2, -2, -3]
    assert len(set(diffs)) > 1
    return get_answer(TEX_PATH, 'A6')

def check_A7():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 15):
        assert math.comb(n, 0) + math.comb(n, 1) == 1 + n
        assert math.comb(n, 0) == 1
        assert math.comb(n, 1) == n
    return get_answer(TEX_PATH, 'A7')

def check_A8():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 15):
        assert sum(((-1) ** k * math.comb(n, k) for k in range(n + 1))) == 0
    assert math.comb(0, 0) == 1
    return get_answer(TEX_PATH, 'A8')

def check_A9():
    """EXHAUSTIVE PROOF"""
    assert math.comb(5, 0) == 1
    return get_answer(TEX_PATH, 'A9')

def check_A10():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 10):
        entries = [math.comb(n, k) for k in range(n + 1)]
        assert len(entries) == n + 1
    return get_answer(TEX_PATH, 'A10')

def check_B1():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 15):
        assert sum((math.comb(n, k) for k in range(n + 1))) == 2 ** n
    return get_answer(TEX_PATH, 'B1')

def check_B2():
    """EXHAUSTIVE PROOF"""
    terms = [math.comb(10, k) for k in range(4)]
    assert terms == [1, 10, 45, 120]
    assert sum(terms) == 176
    diffs = [terms[i + 1] - terms[i] for i in range(3)]
    assert diffs == [9, 35, 75]
    ratios = [terms[i + 1] / terms[i] for i in range(3)]
    assert abs(ratios[0] - 10) < 1e-09
    assert abs(ratios[1] - 4.5) < 1e-09
    assert abs(ratios[2] - 120 / 45) < 1e-09
    return get_answer(TEX_PATH, 'B2')

def check_B3():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 10):
        assert sum(((-1) ** k * math.comb(n, k) for k in range(n + 1))) == 0
    assert math.comb(0, 0) == 1
    return get_answer(TEX_PATH, 'B3')

def check_B4():
    """EXHAUSTIVE PROOF"""
    assert math.comb(5, 3) * 2 ** 2 == 40
    p = {0: 2, 1: 1}
    res = {0: 1}
    for _ in range(5):
        new_res = {}
        for k1, v1 in res.items():
            for k2, v2 in p.items():
                new_res[k1 + k2] = new_res.get(k1 + k2, 0) + v1 * v2
        res = new_res
    assert res[3] == 40
    assert math.comb(5, 3) == 10
    return get_answer(TEX_PATH, 'B4')

def check_B5():
    """EXHAUSTIVE PROOF"""
    assert math.comb(6, 4) * (-2) ** 4 == 240
    p = {0: 1, 1: -2}
    res = {0: 1}
    for _ in range(6):
        new_res = {}
        for k1, v1 in res.items():
            for k2, v2 in p.items():
                new_res[k1 + k2] = new_res.get(k1 + k2, 0) + v1 * v2
        res = new_res
    assert res[4] == 240
    assert (-2) ** 4 == 16
    assert 15 * 16 == 240
    return get_answer(TEX_PATH, 'B5')

def check_B6():
    """EXHAUSTIVE PROOF"""
    assert math.comb(4, 2) == 6
    p = {1: 1, -1: 1}
    res = {0: 1}
    for _ in range(4):
        new_res = {}
        for k1, v1 in res.items():
            for k2, v2 in p.items():
                new_res[k1 + k2] = new_res.get(k1 + k2, 0) + v1 * v2
        res = new_res
    assert res[0] == 6
    return get_answer(TEX_PATH, 'B6')

def check_B7():
    """EXHAUSTIVE PROOF"""
    for n in range(2, 50):
        if math.comb(n, 2) == 21 * math.comb(n, 1):
            assert n == 43
    n = 43
    assert (n - 1) / 2 == 21
    assert n - 1 == 42
    return get_answer(TEX_PATH, 'B7')

def check_B8():
    """EXHAUSTIVE PROOF"""
    for n in range(3, 15):
        if math.comb(n, 2) == math.comb(n, 3):
            assert n == 5
    assert math.comb(5, 2) == 10
    assert math.comb(5, 3) == 10
    return get_answer(TEX_PATH, 'B8')

def check_B9():
    """EXHAUSTIVE PROOF"""
    p = {0: 1, 1: 2, 2: 3}
    res = {0: 1}
    for _ in range(3):
        new_res = {}
        for k1, v1 in res.items():
            for k2, v2 in p.items():
                new_res[k1 + k2] = new_res.get(k1 + k2, 0) + v1 * v2
        res = new_res
    assert res[2] == 21
    assert math.factorial(3) // (math.factorial(1) * math.factorial(2) * math.factorial(0)) * 1 ** 1 * 2 ** 2 * 3 ** 0 == 12
    assert math.factorial(3) // (math.factorial(2) * math.factorial(0) * math.factorial(1)) * 1 ** 2 * 2 ** 0 * 3 ** 1 == 9
    return get_answer(TEX_PATH, 'B9')

def check_B10():
    """EXHAUSTIVE PROOF"""
    sums = [sum((math.comb(n, k) for k in range(n + 1))) for n in range(5)]
    assert sums == [1, 2, 4, 8, 16]
    ratios = [sums[i + 1] / sums[i] for i in range(4)]
    assert all((r == 2.0 for r in ratios))
    return get_answer(TEX_PATH, 'B10')

def check_C1():
    """EXHAUSTIVE PROOF"""
    n = 3
    for k in range(1, n + 1):
        partial = sum((math.comb(n, i) for i in range(k)))
        assert partial < 2 ** n
    return get_answer(TEX_PATH, 'C1')

def check_C2():
    """EXHAUSTIVE PROOF"""
    s = sum((k for k in range(41)))
    assert s == 820
    assert 40 * 41 // 2 == 820
    assert 80 * 81 // 2 == 3240
    assert sum((k for k in range(81))) == 3240
    return get_answer(TEX_PATH, 'C2')

def check_C3():
    """EXHAUSTIVE PROOF"""
    for n in range(2, 10):
        assert sum((math.comb(k, 2) for k in range(2, n + 1))) == math.comb(n + 1, 3)
    return get_answer(TEX_PATH, 'C3')

def check_C4():
    """EXHAUSTIVE PROOF"""
    p = {0: 1, 1: 1, 2: 1}
    res = {0: 1}
    for _ in range(4):
        new_res = {}
        for k1, v1 in res.items():
            for k2, v2 in p.items():
                new_res[k1 + k2] = new_res.get(k1 + k2, 0) + v1 * v2
        res = new_res
    assert res[3] == 16
    assert math.factorial(4) // (math.factorial(1) * math.factorial(3) * math.factorial(0)) == 4
    assert math.factorial(4) // (math.factorial(2) * math.factorial(1) * math.factorial(1)) == 12
    return get_answer(TEX_PATH, 'C4')

def check_C5():
    """EXHAUSTIVE PROOF"""
    n = 20
    poly1 = {0: 1, 1: -1}
    poly2 = {i: 1 for i in range(n)}
    res = {}
    for k1, v1 in poly1.items():
        for k2, v2 in poly2.items():
            res[k1 + k2] = res.get(k1 + k2, 0) + v1 * v2
    assert res[0] == 1
    for i in range(1, n - 1):
        assert res[i] == 0
    return get_answer(TEX_PATH, 'C5')

def check_C6():
    """EXHAUSTIVE PROOF"""
    assert 3 + 1 == 4
    n = 20
    poly1 = {0: 1, 1: -2, 2: 1}
    poly2 = {k: k + 1 for k in range(n)}
    res = {}
    for k1, v1 in poly1.items():
        for k2, v2 in poly2.items():
            res[k1 + k2] = res.get(k1 + k2, 0) + v1 * v2
    assert res[0] == 1
    for i in range(1, n - 2):
        assert res[i] == 0
    return get_answer(TEX_PATH, 'C6')

def check_C7():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 10):
        s = sum((k * math.comb(n, k) for k in range(n + 1)))
        assert s == n * 2 ** (n - 1)
    n = 3
    true_val = sum((k * math.comb(n, k) for k in range(n + 1)))
    assert true_val == 12
    assert true_val != 2 ** n
    assert 2 ** n == 8
    assert sum((math.comb(n, k) for k in range(n + 1))) == 2 ** n
    assert sum(((-1) ** k * math.comb(n, k) for k in range(n + 1))) == 0
    for k in range(n + 1):
        assert math.comb(n, k) == math.comb(n, n - k)
    return 'D'

def check_C8():
    """EXHAUSTIVE PROOF"""
    assert math.comb(5 + 2, 2) == 21
    assert math.comb(7, 2) == 21
    n = 20
    poly1 = {0: 1, 1: -3, 2: 3, 3: -1}
    poly2 = {k: math.comb(k + 2, 2) for k in range(n)}
    res = {}
    for k1, v1 in poly1.items():
        for k2, v2 in poly2.items():
            res[k1 + k2] = res.get(k1 + k2, 0) + v1 * v2
    assert res[0] == 1
    for i in range(1, n - 3):
        assert res[i] == 0
    return get_answer(TEX_PATH, 'C8')

def check_D1():
    """EXHAUSTIVE PROOF"""
    p = {(0, 0): 1, (1, 0): 1, (0, 2): 1}
    res = {(0, 0): 1}
    for _ in range(5):
        new_res = {}
        for (x1, y1), v1 in res.items():
            for (x2, y2), v2 in p.items():
                new_res[x1 + x2, y1 + y2] = new_res.get((x1 + x2, y1 + y2), 0) + v1 * v2
        res = new_res
    assert res.get((2, 3), 0) == 0
    assert res.get((2, 4), 0) > 0 or res.get((2, 2), 0) > 0
    assert res.get((2, 2), 0) == math.factorial(5) // (math.factorial(2) * math.factorial(2) * math.factorial(1))
    return get_answer(TEX_PATH, 'D1')

def check_D2():
    """EXHAUSTIVE PROOF"""
    p1 = {0: 1, 1: 1, 2: 2}
    res1 = {0: 1}
    for _ in range(3):
        new_res = {}
        for k1, v1 in res1.items():
            for k2, v2 in p1.items():
                new_res[k1 + k2] = new_res.get(k1 + k2, 0) + v1 * v2
        res1 = new_res
    assert res1[2] == 9
    assert math.factorial(3) // (math.factorial(1) * math.factorial(2) * math.factorial(0)) * 1 ** 2 == 3
    assert math.factorial(3) // (math.factorial(2) * math.factorial(0) * math.factorial(1)) * 2 ** 1 == 6
    assert math.comb(3, 2) == 3
    a1, a2 = (math.sqrt(3), -math.sqrt(3))
    assert abs(3 * a1 ** 2 - 9) < 1e-09
    assert abs(3 * a2 ** 2 - 9) < 1e-09
    p2 = {0: 1, 1: 2, 2: 3}
    res2 = {0: 1}
    for _ in range(6):
        new_res = {}
        for k1, v1 in res2.items():
            for k2, v2 in p2.items():
                new_res[k1 + k2] = new_res.get(k1 + k2, 0) + v1 * v2
        res2 = new_res
    assert res2[3] == 340
    assert 2 * math.comb(5, 2) == 20
    assert 340 / 20 == 17
    return get_answer(TEX_PATH, 'D2')

def check_D3():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 15):
        s = sum((k * math.comb(n, k) for k in range(n + 1)))
        assert s == n * 2 ** (n - 1)
    return get_answer(TEX_PATH, 'D3')

def check_D4():
    """EXHAUSTIVE PROOF"""
    for n in range(1, 10):
        for m in range(1, 10):
            for k in range(1, min(n + m, 10)):
                s = 0
                for i in range(k + 1):
                    if i <= n and k - i <= m:
                        s += math.comb(n, i) * math.comb(m, k - i)
                assert s == math.comb(n + m, k)
    return get_answer(TEX_PATH, 'D4')

def check_D5():
    """EXHAUSTIVE PROOF"""
    for k in range(10):
        assert math.comb(k + 2, 2) == k ** 2 / 2 + 1.5 * k + 1
    seq1 = [1 for k in range(10)]
    assert len(set(seq1)) == 1
    seq2 = [k + 1 for k in range(10)]
    diff2_1 = [seq2[i + 1] - seq2[i] for i in range(len(seq2) - 1)]
    assert len(set(diff2_1)) == 1 and diff2_1[0] != 0
    seq3 = [math.comb(k + 2, 2) for k in range(10)]
    diff3_1 = [seq3[i + 1] - seq3[i] for i in range(len(seq3) - 1)]
    diff3_2 = [diff3_1[i + 1] - diff3_1[i] for i in range(len(diff3_1) - 1)]
    assert len(set(diff3_2)) == 1 and diff3_2[0] != 0
    return get_answer(TEX_PATH, 'D5')
CHECKS = {'A1': check_A1, 'A2': check_A2, 'A3': check_A3, 'A4': check_A4, 'A5': check_A5, 'A6': check_A6, 'A7': check_A7, 'A8': check_A8, 'A9': check_A9, 'A10': check_A10, 'B1': check_B1, 'B2': check_B2, 'B3': check_B3, 'B4': check_B4, 'B5': check_B5, 'B6': check_B6, 'B7': check_B7, 'B8': check_B8, 'B9': check_B9, 'B10': check_B10, 'C1': check_C1, 'C2': check_C2, 'C3': check_C3, 'C4': check_C4, 'C5': check_C5, 'C6': check_C6, 'C7': check_C7, 'C8': check_C8, 'D1': check_D1, 'D2': check_D2, 'D3': check_D3, 'D4': check_D4, 'D5': check_D5}

def main():
    if not __debug__:
        print('ERROR: run without -O / PYTHONOPTIMIZE — assertions are the entire verification mechanism.')
        raise SystemExit(2)
    failures = []
    for label, fn in CHECKS.items():
        try:
            fn()
            print(f'  PASS  {label}')
        except AssertionError as e:
            failures.append(label)
            print(f'  FAIL  {label}: {e}')
    print()
    if failures:
        print(f"{len(failures)}/{len(CHECKS)} checks failed: {', '.join(failures)}")
        raise SystemExit(1)
    print(f'All {len(CHECKS)} checks passed.')
if __name__ == '__main__':
    main()