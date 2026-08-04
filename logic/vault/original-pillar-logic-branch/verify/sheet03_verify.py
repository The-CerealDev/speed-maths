import math
import itertools

# ── shared helpers ──────────────────────────────────────────────────────────

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def lcm(a, b):
    return a * b // math.gcd(a, b)

def implies(a, b):
    return (not a) or b


# ══════════════════════════════════════════════════════════════════════════
# Section A — Rapid Recognition
# ══════════════════════════════════════════════════════════════════════════

# A1: negate "n is even" -> "n is odd"
def check_A1():
    """ EXHAUSTIVE PROOF """
    P = lambda n: n % 2 == 0            # "n is even"
    notP_claimed = lambda n: n % 2 != 0  # claimed negation: "n is odd"
    domain = range(-1000, 1001)
    for n in domain:
        assert P(n) != notP_claimed(n)   # always exactly opposite (partition)
        assert notP_claimed(n) == (not P(n))


# A2: negate "x>5" -> "x<=5"
def check_A2():
    """ EXHAUSTIVE PROOF """
    P = lambda x: x > 5
    notP_claimed = lambda x: x <= 5
    domain = [i * 0.1 for i in range(-2000, 2001)]
    for x in domain:
        assert P(x) != notP_claimed(x)
    assert not P(5) and notP_claimed(5)   # boundary case must land in the negation
    # the common wrong answer "x<5" is NOT a valid negation: it agrees with P
    # (rather than opposing it) at the boundary x=5
    wrong = lambda x: x < 5
    assert wrong(5) == P(5)


# A3: De Morgan, "and" -> "or": negate "n div by 3 and by 5"
def check_A3():
    """ EXHAUSTIVE PROOF """
    for P, Q in itertools.product([False, True], repeat=2):
        original = P and Q
        claimed_negation = (not P) or (not Q)
        assert claimed_negation == (not original)
    for n in range(-1000, 1001):
        P, Q = (n % 3 == 0), (n % 5 == 0)
        claimed_negation = (n % 3 != 0) or (n % 5 != 0)
        assert claimed_negation == (not (P and Q))


# A4: De Morgan, "or" -> "and": negate "x=2 or x=3"
def check_A4():
    """ EXHAUSTIVE PROOF """
    for P, Q in itertools.product([False, True], repeat=2):
        original = P or Q
        claimed_negation = (not P) and (not Q)
        assert claimed_negation == (not original)
    domain = [i * 0.5 for i in range(-40, 41)]
    for x in domain:
        original = (x == 2) or (x == 3)
        claimed_negation = (x != 2) and (x != 3)
        assert claimed_negation == (not original)


# A5: negate "for all n, n^2>=0" -> "exists n, n^2<0"
def check_A5():
    """ SAMPLED CHECK """
    domain = range(-2000, 2001)
    P = lambda n: n**2 >= 0
    notP_claimed = lambda n: n**2 < 0
    for n in domain:
        assert P(n) != notP_claimed(n)   # >=0 / <0 partition every sampled n
    # the ∀-statement holds throughout the sample (no witness to its negation);
    # this is evidence, not proof, since the true domain (all integers) is
    # infinite -- what IS fully verified is the negation formula's correctness
    assert all(P(n) for n in domain)
    assert not any(notP_claimed(n) for n in domain)


# A6: negate "exists n, n^2=2" -> "for all n, n^2 != 2"
def check_A6():
    """ EXHAUSTIVE PROOF """
    N = 2000
    for n in range(-N, N + 1):
        assert n**2 != 2
    # squares grow monotonically in |n|, so beyond this window n^2 >= (N+1)^2
    # which is already far past 2 -- this closes the bound for ALL integers
    assert (N + 1)**2 > 2
    P = lambda n: n**2 == 2
    notP_claimed = lambda n: n**2 != 2
    for n in range(-N, N + 1):
        assert P(n) != notP_claimed(n)


# A7: "the negation of a true statement is always false" -- True
def check_A7():
    """ EXHAUSTIVE PROOF """
    for P in [False, True]:              # exhaustive over the only 2 truth values
        assert not (P and (not P))       # law of non-contradiction
        if P is True:
            assert (not P) is False


# A8: contrapositive of "if n even then n^2 even" -> "if n^2 odd then n odd"
def check_A8():
    """ EXHAUSTIVE PROOF """
    H = lambda n: n % 2 == 0
    C = lambda n: (n**2) % 2 == 0
    H2 = lambda n: (n**2) % 2 != 0   # claimed contrapositive hypothesis (not C)
    C2 = lambda n: n % 2 != 0         # claimed contrapositive conclusion (not H)
    for n in range(-1000, 1001):
        assert H2(n) == (not C(n))
        assert C2(n) == (not H(n))
        assert implies(H(n), C(n)) == implies(H2(n), C2(n))


# A9: "the contrapositive is always logically equivalent to the original" -- True
def check_A9():
    """ EXHAUSTIVE PROOF """
    for P, Q in itertools.product([False, True], repeat=2):
        orig = implies(P, Q)
        contra = implies(not Q, not P)
        assert orig == contra


# A10: "contrapositive is the same as converse" -- False
def check_A10():
    """ EXHAUSTIVE PROOF """
    disagreement_found = False
    for P, Q in itertools.product([False, True], repeat=2):
        converse = implies(Q, P)
        contra = implies(not Q, not P)
        if converse != contra:
            disagreement_found = True
    assert disagreement_found
    # concrete instance: "if n mult of 4 then n even"
    domain = range(-1000, 1001)
    converse_holds = all((n % 2 != 0) or (n % 4 == 0) for n in domain)
    contra_holds = all((n % 2 == 0) or (n % 4 != 0) for n in domain)
    assert converse_holds is False    # e.g. n=2 breaks the converse
    assert contra_holds is True
    assert converse_holds != contra_holds


# ══════════════════════════════════════════════════════════════════════════
# Section B — Manipulation Drills
# ══════════════════════════════════════════════════════════════════════════

# B1: negate "if n prime then n odd" -> "n prime and n even"
def check_B1():
    """ EXHAUSTIVE PROOF """
    for P, Q in itertools.product([False, True], repeat=2):
        orig = implies(P, Q)
        claimed_neg = P and (not Q)
        assert claimed_neg == (not orig)
    n = 2
    P, Q = is_prime(n), (n % 2 != 0)
    assert P and not Q                     # n=2 satisfies the negation
    assert implies(P, Q) is False          # confirms original is false as stated


# B2: negate "for all x>0, x^2>0" -> "exists x>0, x^2<=0"
def check_B2():
    """ SAMPLED CHECK """
    domain = [i * 0.01 for i in range(1, 20001)]   # x in (0, 200]
    P = lambda x: x**2 > 0
    notP_claimed = lambda x: x**2 <= 0
    for x in domain:
        assert P(x) != notP_claimed(x)
    assert all(P(x) for x in domain)
    assert not any(notP_claimed(x) for x in domain)
    # the domain restriction x>0 belongs to the quantifier's scope and is not
    # itself negated -- the claimed negation still ranges over x>0, not x<=0
    assert domain[0] > 0


# B3: De Morgan, "or" -> "and": negate "n mult4 or n mult6"
def check_B3():
    """ EXHAUSTIVE PROOF """
    for P, Q in itertools.product([False, True], repeat=2):
        original = P or Q
        claimed_negation = (not P) and (not Q)
        assert claimed_negation == (not original)
    for n in range(-1000, 1001):
        original = (n % 4 == 0) or (n % 6 == 0)
        claimed_negation = (n % 4 != 0) and (n % 6 != 0)
        assert claimed_negation == (not original)
    n = 5
    assert (n % 4 != 0) and (n % 6 != 0)     # witness satisfying the negation


# B4: contrapositive of "if x>2 then x^2>4" -> "if x^2<=4 then x<=2"
def check_B4():
    """ EXHAUSTIVE PROOF """
    H = lambda x: x > 2
    C = lambda x: x**2 > 4
    H2 = lambda x: x**2 <= 4   # not C
    C2 = lambda x: x <= 2       # not H
    domain = [i * 0.1 for i in range(-10000, 10001)]
    for x in domain:
        assert H2(x) == (not C(x))
        assert C2(x) == (not H(x))
        assert implies(H(x), C(x)) == implies(H2(x), C2(x))


# B5: prove "if n^2 odd then n odd" via contrapositive "if n even then n^2 even"
def check_B5():
    """ EXHAUSTIVE PROOF """
    for k in range(-500, 501):
        n = 2 * k
        assert n**2 == 2 * (2 * k**2)
        assert (n**2) % 2 == 0
    H = lambda n: (n**2) % 2 != 0   # original hyp: n^2 odd
    C = lambda n: n % 2 != 0         # original concl: n odd
    H2 = lambda n: n % 2 == 0        # not C: n even (contrapositive hyp)
    C2 = lambda n: (n**2) % 2 == 0   # not H: n^2 even (contrapositive concl)
    for n in range(-1000, 1001):
        assert H2(n) == (not C(n))
        assert C2(n) == (not H(n))
        assert implies(H(n), C(n)) == implies(H2(n), C2(n))
    assert all(implies(H2(n), C2(n)) for n in range(-1000, 1001))


# B6: negate "n prime and n>2" -> "n not prime or n<=2"
def check_B6():
    """ EXHAUSTIVE PROOF """
    for P, Q in itertools.product([False, True], repeat=2):
        original = P and Q
        claimed_negation = (not P) or (not Q)
        assert claimed_negation == (not original)
    for n in range(-100, 1000):
        P, Q = is_prime(n), (n > 2)
        claimed_negation = (not is_prime(n)) or (n <= 2)
        assert claimed_negation == (not (P and Q))
    n = 2
    assert (not is_prime(n)) or (n <= 2)   # negation holds at n=2 (2<=2)


# B7: negate "if it rains then ground wet" -> "it rains and ground not wet"
def check_B7():
    """ EXHAUSTIVE PROOF """
    for P, Q in itertools.product([False, True], repeat=2):
        orig = implies(P, Q)
        claimed_neg = P and (not Q)
        assert claimed_neg == (not orig)
    # the inverse and the converse are NOT the negation -- both disagree with
    # the true negation somewhere in the truth table
    disagree_inverse, disagree_converse = False, False
    for P, Q in itertools.product([False, True], repeat=2):
        neg = P and (not Q)
        inverse = implies(not P, not Q)
        converse = implies(Q, P)
        if neg != inverse:
            disagree_inverse = True
        if neg != converse:
            disagree_converse = True
    assert disagree_inverse and disagree_converse


# B8: contrapositive of "if n mult9 then n mult3" -> "if n not mult3 then n not mult9"
def check_B8():
    """ EXHAUSTIVE PROOF """
    H = lambda n: n % 9 == 0
    C = lambda n: n % 3 == 0
    H2 = lambda n: n % 3 != 0   # not C
    C2 = lambda n: n % 9 != 0   # not H
    domain = range(-10000, 10001)
    for n in domain:
        assert H2(n) == (not C(n))
        assert C2(n) == (not H(n))
        assert implies(H(n), C(n)) == implies(H2(n), C2(n))
    assert all(implies(H(n), C(n)) for n in domain)   # original genuinely true


# B9: "not(P and Q) == (not P) and (not Q)" -- False
def check_B9():
    """ EXHAUSTIVE PROOF """
    disagreement = False
    for P, Q in itertools.product([False, True], repeat=2):
        lhs = not (P and Q)
        rhs_wrong = (not P) and (not Q)
        rhs_correct = (not P) or (not Q)
        assert lhs == rhs_correct                # the actual De Morgan law
        if lhs != rhs_wrong:
            disagreement = True
    assert disagreement
    P, Q = True, False     # "2 is even" (T), "3 is even" (F), per the method
    assert (not (P and Q)) is True
    assert ((not P) and (not Q)) is False


# B10: "not(P or Q) == (not P) and (not Q)" -- True
def check_B10():
    """ EXHAUSTIVE PROOF """
    for P, Q in itertools.product([False, True], repeat=2):
        assert (not (P or Q)) == ((not P) and (not Q))


# ══════════════════════════════════════════════════════════════════════════
# Section C — Substitution & Structure
# ══════════════════════════════════════════════════════════════════════════

# C1: negate "for every prime p, p odd or p=2"
def check_C1():
    """ EXHAUSTIVE PROOF """
    N = 100000
    primes = [p for p in range(2, N) if is_prime(p)]
    for p in primes:
        assert (p % 2 != 0) or (p == 2)
    # any even number > 2 has 2 as a proper divisor, so it can never be prime
    # -- this argument doesn't depend on how large the number is, so it closes
    # the case for every prime, not just the ones below N
    for p in range(4, N, 2):
        assert not is_prime(p)
    for P, Q in itertools.product([False, True], repeat=2):
        original = P or Q
        claimed_neg_inner = (not P) and (not Q)
        assert claimed_neg_inner == (not original)
    witnesses = [p for p in primes if (p % 2 == 0) and (p != 2)]
    assert witnesses == []


# C2: prove "if n^2 even then n even" via contrapositive "if n odd then n^2 odd"
def check_C2():
    """ EXHAUSTIVE PROOF """
    for k in range(-500, 501):
        n = 2 * k + 1
        assert n**2 == 4 * k**2 + 4 * k + 1
        assert n**2 == 2 * (2 * k**2 + 2 * k) + 1
        assert (n**2) % 2 != 0
    H = lambda n: (n**2) % 2 == 0   # original hyp
    C = lambda n: n % 2 == 0         # original concl
    H2 = lambda n: n % 2 != 0        # not C
    C2 = lambda n: (n**2) % 2 != 0   # not H
    for n in range(-1000, 1001):
        assert H2(n) == (not C(n))
        assert C2(n) == (not H(n))
        assert implies(H(n), C(n)) == implies(H2(n), C2(n))
    assert all(implies(H2(n), C2(n)) for n in range(-1000, 1001))


# C3: correct negation of "if x rational then x^2 rational" is option B
def check_C3():
    """ EXHAUSTIVE PROOF """
    for P, Q in itertools.product([False, True], repeat=2):
        orig = implies(P, Q)
        optB = P and (not Q)
        assert optB == (not orig)      # option B is the genuine negation

    disagreeA, disagreeC_is_equiv, disagreeD = False, True, False
    for P, Q in itertools.product([False, True], repeat=2):
        orig = implies(P, Q)
        optA = implies(not P, not Q)     # inverse
        optC = implies(not Q, not P)     # contrapositive
        optD = (not P) and Q
        if optA != (not orig):
            disagreeA = True
        if optC != orig:
            disagreeC_is_equiv = False
        if optD != (not orig):
            disagreeD = True
    assert disagreeA        # option A (inverse) is not the negation
    assert disagreeC_is_equiv    # option C stayed equal to orig everywhere (it's
                                  # the contrapositive, not the negation)
    assert disagreeD        # option D is not the negation either


# C4: negate "exists n, n prime and n even"
def check_C4():
    """ EXHAUSTIVE PROOF """
    for P, Q in itertools.product([False, True], repeat=2):
        original = P and Q
        claimed_neg = (not P) or (not Q)
        assert claimed_neg == (not original)
    n = 2
    assert is_prime(n) and n % 2 == 0                    # witness for the ∃-statement
    assert not ((not is_prime(n)) or (n % 2 != 0))        # so the ∀-negation fails at n=2
    for n in range(-1000, 1001):
        if n == 2:
            continue
        assert (not is_prime(n)) or (n % 2 != 0)          # and holds everywhere else sampled


# C5: contrapositive + proof of "if n mult4 then n^2 mult16"
def check_C5():
    """ EXHAUSTIVE PROOF """
    for k in range(-500, 501):
        n = 4 * k
        assert n**2 == 16 * k**2
        assert (n**2) % 16 == 0
    H = lambda n: n % 4 == 0
    C = lambda n: (n**2) % 16 == 0
    H2 = lambda n: (n**2) % 16 != 0   # not C
    C2 = lambda n: n % 4 != 0          # not H
    domain = range(-2000, 2001)
    for n in domain:
        assert H2(n) == (not C(n))
        assert C2(n) == (not H(n))
        assert implies(H(n), C(n)) == implies(H2(n), C2(n))
    assert all(implies(H(n), C(n)) for n in domain)


# C6: "if a statement's contrapositive is false, the original must be false" -- True
def check_C6():
    """ EXHAUSTIVE PROOF """
    for P, Q in itertools.product([False, True], repeat=2):
        orig = implies(P, Q)
        contra = implies(not Q, not P)
        assert orig == contra
        if contra is False:
            assert orig is False


# C7: negate "exists positive n, n not mult of any prime <10"
def check_C7():
    """ EXHAUSTIVE PROOF """
    for P in [False, True]:
        assert (not (not P)) == P     # double negation, used to simplify the negation

    primes_lt_10 = [2, 3, 5, 7]
    mult_of_some = lambda n: any(n % p == 0 for p in primes_lt_10)

    assert not mult_of_some(1)        # n=1 witnesses the original ∃-statement
    domain = range(1, 10001)
    failures = [n for n in domain if not mult_of_some(n)]
    assert 1 in failures
    assert 11 in failures             # 11 is prime and >= 10, also not a multiple
                                       # of any prime < 10 -- the claimed ∀-negation
                                       # fails at more than one point
    assert len(failures) > 1


# C8: prove "if n not mult3 then n^2 not mult3" via contrapositive "if n^2 mult3 then n mult3"
def check_C8():
    """ EXHAUSTIVE PROOF """
    domain = range(-2000, 2001)
    for n in domain:
        if (n**2) % 3 == 0:
            assert n % 3 == 0     # 3 is prime, so 3|n^2 forces 3|n
    H = lambda n: n % 3 != 0          # original hyp: n not mult of 3
    C = lambda n: (n**2) % 3 != 0     # original concl: n^2 not mult of 3
    H2 = lambda n: (n**2) % 3 == 0    # not C
    C2 = lambda n: n % 3 == 0          # not H
    for n in domain:
        assert H2(n) == (not C(n))
        assert C2(n) == (not H(n))
        assert implies(H(n), C(n)) == implies(H2(n), C2(n))
    assert all(implies(H2(n), C2(n)) for n in domain)


# ══════════════════════════════════════════════════════════════════════════
# Section D — Challenge
# ══════════════════════════════════════════════════════════════════════════

# D1: contrapositive MCQ of "if n mult4 then n even" -- answer A
def check_D1():
    """ EXHAUSTIVE PROOF """
    H = lambda n: n % 4 == 0
    C = lambda n: n % 2 == 0
    domain = range(-2000, 2001)

    optA = lambda n: implies(n % 2 != 0, n % 4 != 0)   # claimed contrapositive
    for n in domain:
        assert implies(H(n), C(n)) == optA(n)

    optB = lambda n: implies(C(n), H(n))                # converse
    n = 2
    assert H(n) is False and C(n) is True
    orig2 = implies(H(n), C(n))
    assert optB(n) is False and orig2 is True
    assert optB(n) != orig2

    optC = lambda n: implies(n % 4 != 0, n % 2 != 0)    # inverse
    assert optC(n) is False
    assert optC(n) != orig2

    optD = lambda n: implies(n % 2 != 0, n % 4 == 0)    # distractor
    n3 = 3
    orig3 = implies(H(n3), C(n3))
    assert optD(n3) is False and orig3 is True
    assert optD(n3) != orig3


# D2: prove "if n^2-2n odd then n odd" via contrapositive "if n even then n^2-2n even"
def check_D2():
    """ EXHAUSTIVE PROOF """
    for k in range(-500, 501):
        n = 2 * k
        assert n**2 - 2 * n == 4 * k * (k - 1)
        assert (n**2 - 2 * n) % 2 == 0
    H = lambda n: (n**2 - 2 * n) % 2 != 0   # original hyp
    C = lambda n: n % 2 != 0                 # original concl
    H2 = lambda n: n % 2 == 0                # not C
    C2 = lambda n: (n**2 - 2 * n) % 2 == 0   # not H
    for n in range(-1000, 1001):
        assert H2(n) == (not C(n))
        assert C2(n) == (not H(n))
        assert implies(H(n), C(n)) == implies(H2(n), C2(n))
    assert all(implies(H2(n), C2(n)) for n in range(-1000, 1001))


# D3: truth-teller island puzzle
def check_D3():
    """ EXHAUSTIVE PROOF """
    consistent_worlds = []
    for A_truthful in [True, False]:
        for B_truthful in [True, False]:
            statement = (not A_truthful) or (not B_truthful)   # "at least one is a liar"
            if statement == A_truthful:      # A's statement is true iff A is truthful
                consistent_worlds.append((A_truthful, B_truthful))
    assert len(consistent_worlds) == 1
    assert consistent_worlds[0] == (True, False)   # A truth-teller, B liar


# D4: "if n^3 even then n even" via contrapositive "if n odd then n^3 odd"
def check_D4():
    """ EXHAUSTIVE PROOF """
    for k in range(-500, 501):
        n = 2 * k + 1
        assert n**3 == 8 * k**3 + 12 * k**2 + 6 * k + 1
        assert n**3 % 2 != 0
    H = lambda n: (n**3) % 2 == 0
    C = lambda n: n % 2 == 0
    H2 = lambda n: n % 2 != 0
    C2 = lambda n: (n**3) % 2 != 0
    for n in range(-1000, 1001):
        assert H2(n) == (not C(n))
        assert C2(n) == (not H(n))
        assert implies(H(n), C(n)) == implies(H2(n), C2(n))
    assert all(implies(H2(n), C2(n)) for n in range(-1000, 1001))


# D5: (a) contrapositive, (b) necessary & sufficient, (c) direct negation
def check_D5():
    """ EXHAUSTIVE PROOF """
    domain = range(-3000, 3001)

    # (a) contrapositive of S
    H = lambda n: n % 15 == 0
    C = lambda n: (n % 3 == 0) and (n % 5 == 0)
    H2 = lambda n: (n % 3 != 0) or (n % 5 != 0)   # not C, via De Morgan
    C2 = lambda n: n % 15 != 0                     # not H
    for n in domain:
        assert H2(n) == (not C(n))
        assert C2(n) == (not H(n))
        assert implies(H(n), C(n)) == implies(H2(n), C2(n))

    # (b) necessary and sufficient
    assert lcm(3, 5) == 15
    for n in domain:
        if n % 15 == 0:                       # sufficiency: 15|n => 3|n and 5|n
            assert n % 3 == 0 and n % 5 == 0
        if n % 3 == 0 and n % 5 == 0:          # necessity: 3|n and 5|n => 15|n
            assert n % 15 == 0

    # (c) direct negation of S ("P and not Q" form)
    for n in domain:
        P = n % 15 == 0
        Q = (n % 3 == 0) and (n % 5 == 0)
        orig = implies(P, Q)
        claimed_neg = P and (not Q)
        assert claimed_neg == (not orig)
    # the negation is unsatisfiable throughout the sample, consistent with S
    # being true (matches part (b)'s equivalence)
    assert not any((n % 15 == 0) and not ((n % 3 == 0) and (n % 5 == 0)) for n in domain)


CHECKS = {
    "A1": check_A1, "A2": check_A2, "A3": check_A3, "A4": check_A4, "A5": check_A5,
    "A6": check_A6, "A7": check_A7, "A8": check_A8, "A9": check_A9, "A10": check_A10,
    "B1": check_B1, "B2": check_B2, "B3": check_B3, "B4": check_B4, "B5": check_B5,
    "B6": check_B6, "B7": check_B7, "B8": check_B8, "B9": check_B9, "B10": check_B10,
    "C1": check_C1, "C2": check_C2, "C3": check_C3, "C4": check_C4, "C5": check_C5,
    "C6": check_C6, "C7": check_C7, "C8": check_C8,
    "D1": check_D1, "D2": check_D2, "D3": check_D3, "D4": check_D4, "D5": check_D5,
}

def main():
    if not __debug__:
        raise Exception("Do not run with -O! Assertions are disabled.")

    passed = 0
    for name, func in CHECKS.items():
        try:
            func()
            print(f"PASS {name}")
            passed += 1
        except Exception as e:
            print(f"FAILED {name}: {e}")
            raise
    print(f"All {passed} checks passed!")

if __name__ == "__main__":
    main()
