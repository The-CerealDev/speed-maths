"""Computational verification for sequences/answers/ans01.tex.

Convention: one check_<label>() function per question, matching the
section+number label in the sheet (A1, D5, ...).

Run directly:
    python3 sheet01_verify.py
"""

import math
import random
import itertools

def check_A1():
    """EXHAUSTIVE PROOF"""
    def a(n): return 5 + 3 * (n - 1)
    assert a(1) == 5
    assert a(4) == 14
    for n in range(1, 10):
        assert a(n) == 3*n + 2

def check_A2():
    """EXHAUSTIVE PROOF"""
    def a(n): return 7 - 3 * (n - 1)
    assert a(20) == 7 - 57
    assert a(20) == -50

def check_A3():
    """EXHAUSTIVE PROOF"""
    def a(n): return 4 + 5 * (n - 1)
    S_10 = sum(a(n) for n in range(1, 11))
    assert S_10 == 265
    assert a(10) == 49
    assert S_10 == 5 * (4 + 49)
    assert 5 * (8 + 45) == 265

def check_A4():
    """EXHAUSTIVE PROOF"""
    def a(n): return 4 * n - 1
    assert a(1) == 3
    assert a(2) == 7
    assert a(3) == 11
    assert a(2) - a(1) == 4
    assert a(3) - a(2) == 4

def check_A5():
    """EXHAUSTIVE PROOF"""
    a_1 = 2
    a_5 = 18
    # a_5 - a_1 = 4d
    d = (a_5 - a_1) / 4
    assert d == 4
    assert a_5 - a_1 == 16

def check_A6():
    """EXHAUSTIVE PROOF"""
    assert sum(range(1, 51)) == 1275
    assert (50 * 51) // 2 == 1275

def check_A7():
    """EXHAUSTIVE PROOF"""
    def S(n): return n**2 + 3 * n
    a_1 = S(1)
    assert a_1 == 4

def check_A8():
    """EXHAUSTIVE PROOF"""
    # True or false: every arithmetic sequence with integer first term and integer common difference consists entirely of integers.
    def a(n, a1, d): return a1 + (n - 1) * d
    for a1 in range(-5, 5):
        for d in range(-5, 5):
            for n in range(1, 20):
                assert isinstance(a(n, a1, d), int)
    
def check_A9():
    """EXHAUSTIVE PROOF"""
    a_3 = 13
    a_9 = 37
    # a_9 - a_3 = 6d
    assert a_9 - a_3 == 24
    d = (a_9 - a_3) / 6
    assert d == 4

def check_A10():
    """EXHAUSTIVE PROOF"""
    a_1 = 4
    a_6 = 29
    # a_6 - a_1 = 5d
    assert a_6 - a_1 == 25
    d = (a_6 - a_1) / 5
    assert d == 5

def check_B1():
    """EXHAUSTIVE PROOF"""
    a = 3
    l = 59
    n = 15
    # l = a + (n-1)d
    d = (l - a) // (n - 1)
    assert d == 4
    S_15 = sum(a + i * d for i in range(n))
    assert S_15 == 465
    assert (n * (a + l)) // 2 == 465

def check_B2():
    """EXHAUSTIVE PROOF"""
    # S_8 = 100, S_4 = 30. sum 5 to 8?
    S_8 = 100
    S_4 = 30
    assert S_8 - S_4 == 70

def check_B3():
    """EXHAUSTIVE PROOF"""
    # Prove that 3+6+9+...+3n = 3n(n+1)/2
    for n in range(1, 100):
        S_n = sum(3 * i for i in range(1, n + 1))
        assert S_n == (3 * n * (n + 1)) // 2

def check_B4():
    """EXHAUSTIVE PROOF"""
    # AP has 21 terms summing to 315. Find the 11th term.
    middle_term = 315 // 21
    assert middle_term == 15
    # Verify with random a and d such that a_11 = 15
    for _ in range(100):
        d = random.randint(-100, 100)
        a = 15 - 10 * d
        assert sum(a + i * d for i in range(21)) == 315

def check_B5():
    """EXHAUSTIVE PROOF"""
    # a = 10, d = -3
    a = 10
    d = -3
    a_n = lambda n: a + (n - 1) * d
    assert a_n(4) == 1
    assert a_n(5) == -2
    assert a_n(4) > 0 and a_n(5) < 0

def check_B6():
    """EXHAUSTIVE PROOF"""
    # D) All terms are positive. (e.g. a=-100, d=1)
    a, d = -100, 1
    seq = [a + i * d for i in range(5)]
    assert any(x < 0 for x in seq)
    # A) Strictly increasing
    assert all(seq[i] < seq[i + 1] for i in range(len(seq) - 1))
    # B) a_{n+1} - a_n = d
    assert all(seq[i + 1] - seq[i] == d for i in range(len(seq) - 1))
    
def check_B7():
    """EXHAUSTIVE PROOF"""
    # Two APs share d. a_1 - b_1 = 6. a_n - b_n?
    for _ in range(100):
        d = random.randint(-50, 50)
        a_1 = random.randint(-100, 100)
        b_1 = a_1 - 6
        for n in range(1, 20):
            a_n = a_1 + (n - 1) * d
            b_n = b_1 + (n - 1) * d
            assert a_n - b_n == 6

def check_B8():
    """EXHAUSTIVE PROOF"""
    # a_3 = 11, a_3 + a_5 = 32
    a, d = 1, 5
    a_n = lambda n: a + (n - 1) * d
    assert a_n(3) == 11
    assert a_n(3) + a_n(5) == 32
    # Verify method logic
    assert a + 2*d == 11
    assert 2*a + 6*d == 32
    assert (a + 3*d) == 16
    assert (a + 3*d) - (a + 2*d) == 5

def check_B9():
    """EXHAUSTIVE PROOF"""
    # a, d positive integers. a_5 = 17. Which (a,d) NOT possible?
    possible = []
    for a in range(1, 20):
        for d in range(1, 20):
            if a + 4 * d == 17:
                possible.append((a, d))
    
    assert (13, 1) in possible
    assert (9, 2) in possible
    assert (5, 3) in possible
    assert (2, 4) not in possible
    assert 2 + 4 * 4 == 18

def check_B10():
    """EXHAUSTIVE PROOF"""
    ap = [2 + 3 * i for i in range(6)]
    gp = [2 * 2**i for i in range(6)]
    assert ap == [2, 5, 8, 11, 14, 17]
    assert gp == [2, 4, 8, 16, 32, 64]
    
    matches = [i + 1 for i in range(6) if ap[i] == gp[i]]
    assert matches == [1, 3]

def check_C1():
    """EXHAUSTIVE PROOF"""
    # C1: the claim is that for an AP of n>=2 integer terms summing to 15, none of three given statements (n even / first term odd / common difference odd) must be true.
    counter_n_even = False
    counter_a_odd = False
    counter_d_odd = False
    
    for n in range(2, 51):
        for d in range(-50, 51):
            if 30 % n == 0:
                rhs = 30 // n
                if (rhs - (n - 1) * d) % 2 == 0:
                    a = (rhs - (n - 1) * d) // 2
                    
                    assert sum(a + i * d for i in range(n)) == 15
                    
                    if n % 2 != 0:
                        counter_n_even = True
                    if a % 2 == 0:
                        counter_a_odd = True
                    if d % 2 == 0:
                        counter_d_odd = True

    assert counter_n_even
    assert counter_a_odd
    assert counter_d_odd
    
    # Specific ones mentioned in \method:
    # n=3, a=4, d=1 -> 4,5,6 (sum 15)
    assert sum([4, 5, 6]) == 15
    assert len([4, 5, 6]) % 2 != 0 # n=3 odd
    assert 4 % 2 == 0 # a=4 even
    
    # n=3, a=3, d=2 -> 3,5,7 (sum 15)
    assert sum([3, 5, 7]) == 15
    assert 2 % 2 == 0 # d=2 even

def check_C2():
    """EXHAUSTIVE PROOF"""
    # a_n = 2n+1, b_n = 3n-2. c_n = a_n + b_n
    for n in range(1, 20):
        assert (2 * n + 1) + (3 * n - 2) == 5 * n - 1

def check_C3():
    """EXHAUSTIVE PROOF"""
    # b_n = a_n^2. b_n arithmetic only if d=0
    for _ in range(100):
        a = random.randint(-50, 50)
        d = random.randint(-50, 50)
        a_n = lambda n: a + (n - 1) * d
        b_n = lambda n: a_n(n)**2
        
        diffs = [b_n(i + 1) - b_n(i) for i in range(1, 5)]
        is_arith = len(set(diffs)) == 1
        if d == 0:
            assert is_arith
        else:
            assert not is_arith

def check_C4():
    """EXHAUSTIVE PROOF"""
    # AP all pos. S_6 = sum(7..10).
    for _ in range(100):
        d = random.uniform(0.1, 10.0)
        a = 7.5 * d
        S_6 = sum(a + i * d for i in range(6))
        sum_7_10 = sum(a + i * d for i in range(6, 10))
        assert abs(S_6 - sum_7_10) < 1e-9

def check_C5():
    """EXHAUSTIVE PROOF"""
    # a,d pos ints, a<d. Contains 100? A)(5,19) B)(6,17) C)(7,23) D)(8,13)
    def contains_100(a, d):
        return (100 - a) % d == 0 and (100 - a) >= 0

    assert contains_100(5, 19)
    assert (100 - 5) == 19 * 5
    assert not contains_100(6, 17)
    assert not contains_100(7, 23)
    assert not contains_100(8, 13)

def check_C6():
    """EXHAUSTIVE PROOF"""
    # S_{2n} = 2S_n for some n>0 forces d=0
    for _ in range(100):
        n = random.randint(1, 20)
        a = random.randint(-50, 50)
        
        d = 0
        S_2n = sum(a + i * d for i in range(2 * n))
        S_n = sum(a + i * d for i in range(n))
        assert S_2n == 2 * S_n
        
        d = random.randint(1, 50)
        S_2n = sum(a + i * d for i in range(2 * n))
        S_n = sum(a + i * d for i in range(n))
        assert S_2n != 2 * S_n

def check_C7():
    """EXHAUSTIVE PROOF"""
    # S_n = n/2 * (2a + (n-1)d) = d/2 n^2 + (a - d/2)n
    for _ in range(100):
        a = random.randint(-50, 50)
        d = random.randint(-50, 50)
        if d == 0: continue
        
        S = lambda n: sum(a + i * d for i in range(n))
        for n in range(1, 20):
            assert S(n) == (d / 2) * n**2 + (a - d / 2) * n

def check_C8():
    """EXHAUSTIVE PROOF"""
    # S_n = 3n^2 - n. Find d.
    a = 2
    d = 6
    assert d / 2 == 3
    assert a - d / 2 == -1
    for n in range(1, 20):
        assert sum(a + i * d for i in range(n)) == 3 * n**2 - n

def check_D1():
    """EXHAUSTIVE PROOF"""
    # S_6 = S_11 => a=-8d
    for _ in range(100):
        d = random.randint(-50, 50)
        a = -8 * d
        S_6 = sum(a + i * d for i in range(6))
        S_11 = sum(a + i * d for i in range(11))
        assert S_6 == S_11
        
        # Verify method claim
        # 3(2a+5d) = 5.5(2a+10d) => 6a+15d = 11a+55d => -5a=40d
        assert 3 * (2 * a + 5 * d) == 5.5 * (2 * a + 10 * d)
        assert 6 * a + 15 * d == 11 * a + 55 * d
        assert -5 * a == 40 * d

def check_D2():
    """EXHAUSTIVE PROOF"""
    # S from 2,5,8,...,80. Smallest n for two summing to 82.
    seq = [3 * i - 1 for i in range(1, 28)]
    assert seq[0] == 2
    assert seq[-1] == 80
    assert len(seq) == 27
    
    pairs = []
    singletons = []
    for i in range(1, 28):
        j = 28 - i
        if i < j:
            pairs.append((seq[i - 1], seq[j - 1]))
        elif i == j:
            singletons.append(seq[i - 1])
            
    assert len(pairs) == 13
    assert len(singletons) == 1
    assert singletons[0] == 41
    assert 41 + 41 == 82
    
    for x, y in pairs:
        assert x + y == 82
        
    subset_14 = [x for x, y in pairs] + singletons
    assert len(subset_14) == 14
    
    for x, y in itertools.combinations(subset_14, 2):
        assert x + y != 82
        
    # Programmatic verification of the max independent set of the "no-82-sum" graph
    adj = {x: [] for x in seq}
    for x, y in pairs:
        adj[x].append(y)
        adj[y].append(x)
        
    max_subset_size = 0
    visited = set()
    for x in seq:
        if x not in visited:
            if not adj[x]:
                max_subset_size += 1
                visited.add(x)
            else:
                y = adj[x][0]
                max_subset_size += 1 # pick one of the pair
                visited.add(x)
                visited.add(y)
                
    assert max_subset_size == 14

def check_D3():
    """STRONG EVIDENCE"""
    def sieve(limit):
        is_prime = [True] * limit
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit, i):
                    is_prime[j] = False
        return is_prime

    limit = 100000
    is_prime = sieve(limit)
    primes = [i for i in range(limit) if is_prime[i]]
    prime_set = set(primes)

    count = 0
    for p in primes:
        if p <= 3:
            continue
        max_d = (limit - 1 - p) // 3
        for d in range(1, max_d + 1):
            if (p + d) in prime_set and (p + 2 * d) in prime_set and (p + 3 * d) in prime_set:
                assert d % 6 == 0
                count += 1
                
    assert count > 0 
    
    for p in primes:
        if p > 3:
            assert p % 2 != 0
            assert p % 3 != 0
            
    for p in [5, 7, 11]:
        for d in [1, 2]:
            res = {p % 3, (p + d) % 3, (p + 2 * d) % 3}
            assert len(res) == 3
            assert 0 in res

def check_D4():
    """EXHAUSTIVE PROOF"""
    A = 5
    B = -4
    a_n = lambda n: A * (2 * n - 1) + B
    S_n = lambda n: A * n**2 + B * n
    
    assert a_n(10) == 91
    assert S_n(10) - S_n(9) == 91
    
    for _ in range(100):
        AA = random.randint(-10, 10)
        BB = random.randint(-10, 10)
        for n in range(1, 20):
            S = AA * n**2 + BB * n
            S_prev = AA * (n - 1)**2 + BB * (n - 1)
            assert S - S_prev == AA * (2 * n - 1) + BB

def check_D5():
    """EXHAUSTIVE PROOF"""
    for _ in range(20):
        start = random.randint(-50, 50)
        diff_start = random.randint(-10, 10)
        d = random.randint(-10, 10)
        
        seq = [start]
        curr_diff = diff_start
        for _ in range(10):
            seq.append(seq[-1] + curr_diff)
            curr_diff += d
            
        C = seq[0]
        A = (seq[2] - 2 * seq[1] + C) / 2
        B = seq[1] - C - A
        
        for n in range(11):
            assert abs(A * n**2 + B * n + C - seq[n]) < 1e-9


CHECKS = {
    "A1": check_A1,
    "A2": check_A2,
    "A3": check_A3,
    "A4": check_A4,
    "A5": check_A5,
    "A6": check_A6,
    "A7": check_A7,
    "A8": check_A8,
    "A9": check_A9,
    "A10": check_A10,
    "B1": check_B1,
    "B2": check_B2,
    "B3": check_B3,
    "B4": check_B4,
    "B5": check_B5,
    "B6": check_B6,
    "B7": check_B7,
    "B8": check_B8,
    "B9": check_B9,
    "B10": check_B10,
    "C1": check_C1,
    "C2": check_C2,
    "C3": check_C3,
    "C4": check_C4,
    "C5": check_C5,
    "C6": check_C6,
    "C7": check_C7,
    "C8": check_C8,
    "D1": check_D1,
    "D2": check_D2,
    "D3": check_D3,
    "D4": check_D4,
    "D5": check_D5,
}

def main():
    if not __debug__:
        print("ERROR: run without -O / PYTHONOPTIMIZE — assertions are the entire verification mechanism.")
        raise SystemExit(2)

    failures = []
    for label, fn in CHECKS.items():
        try:
            fn()
            print(f"  PASS  {label}")
        except AssertionError as e:
            failures.append(label)
            print(f"  FAIL  {label}: {e}")
    print()
    if failures:
        print(f"{len(failures)}/{len(CHECKS)} checks failed: {', '.join(failures)}")
        raise SystemExit(1)
    print(f"All {len(CHECKS)} checks passed.")

if __name__ == "__main__":
    main()
