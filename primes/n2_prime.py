from math import sqrt
from pprint import pprint

from prime_utils import get_primes_less_than as gplt


MAX_PRIME_SAFE = 10000000 #10m

def main():
    # primes = gplt(MAX_PRIME_SAFE)
    n2_primes, _ = get_n2_primes(MAX_PRIME_SAFE)
    # diff_reg = regularity_diff_n2_primes(n2_primes)
    # n_to_m_reg = n_to_m_in_diff_regularity(diff_reg)
    # pprint(n2_primes)
    breakpoint()
    # for idx in range(len(MAX_PRIME_SAFE)):

def get_n2_primes(largest):
    """Find all the primes less than largest that are of the form
    `(n**2 + 1)`, where n is a pos int
    """
    ret = []
    # primes are ordered
    primes = gplt(largest)
    for n in range(largest):
        if (n**2 + 1) > primes[-1]:
            break
        if (n**2 + 1) in primes:
            ret.append(f"{n}**2 + 1 = {n**2 + 1}")
    return ret, primes

def regularity_diff_n2_primes(n2_primes):
    ret = []
    for idx in range(len(n2_primes)):
        try:
            ret.append(n2_primes[idx+1] - n2_primes[idx])
        except IndexError:
            break
    return ret

def n_to_m_in_diff_regularity(diff_reg):
    ret = []
    max_n, max_m = int(sqrt(diff_reg[-1])), 20
    for n in range(2, max_n):
        for m in range(2, max_m):
            if n**m > diff_reg[-1]:
                break
            if n ** m in diff_reg:
                ret.append(f"{n}^{m}")
    return ret
    

if __name__ == "__main__":
    main()