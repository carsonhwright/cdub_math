from pprint import pprint

from prime_utils import get_primes_less_than as gplt

MAX_PRIME = 1000000

def main():
    prime_list = gplt(MAX_PRIME)
    tp = show_twin_primes(prime_list)
    get_tp_diffs(tp)

def show_twin_primes(primes):
    """print and return list of tuples of primes such that each element
    consists of a pair of primes (p, p+2)
    """
    twin_primes = []
    for idx in range(len(primes)):
        try:
            if primes[idx + 1] - primes[idx] == 2:
                twin_primes.append((primes[idx], primes[idx+1]))
        except IndexError:
            pprint(twin_primes)
    return twin_primes

def get_tp_diffs(twins):
    diffs = []
    for idx in range(len(twins)):
        try:
            diffs.append(twins[idx + 1][0] - twins[idx][-1])
        except IndexError:
            break
    pprint(diffs)
    print("If there's a pattern, I don't see it")



if __name__ == "__main__":
    main()