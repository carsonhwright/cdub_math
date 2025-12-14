from time import time_ns
from math import sqrt


def get_primes_less_than(n: float):
    """Return a list of all the prime numbers less than `n`
    TODO This is not optimized, be careful - see https://www.python.org/doc/essays/list2str/  - also see https://en.wikipedia.org/wiki/Sieve_of_Atkin
    TODO This function and all others using large `N` need a memory and processor check (psutil virtual_memory and whatever)


    Params
    ------
    n : float - max value of potential primes to return

    Returns
    -------
    prime_list : list(int) - set of primes less than n
    """
    n = int(n)
    prime_list = []
    for prime_check in range(2,n):
        not_prime = False
        for prime in prime_list:
            if prime ** 2 > prime_check:
                break 
            if prime_check % prime == 0:
                not_prime = True
                break
        if not_prime:
            continue
        else:
            prime_list.append(prime_check)
    return prime_list


def is_prime(n):

    primes = get_primes_less_than(int(sqrt(n))+1)
    not_prime = False
    divisor = 0
    for prime in primes:
        if n % prime == 0:
            not_prime = True
            divisor = prime
            break
    return not not_prime, divisor

def sieveOfAtkin(limit):
    P = [2,3]
    sieve=[False]*(limit+1)
    for x in range(1,int(sqrt(limit))+1):
        for y in range(1,int(sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7 : sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
    for x in range(5,int(sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p] : P.append(p)
    return P

def compare_algorithms(alg_1:callable, alg_2:callable, n):
    time_alg_1 = time_ns()
    alg_1(n)
    time_alg_1 = abs(time_alg_1 - time_ns())
    time_alg_2 = time_ns()
    alg_2(n)
    time_alg_2 = abs(time_alg_2 - time_ns())
    print(f"Time for {alg_1.__name__} : {time_alg_1}")
    print(f"Time for {alg_2.__name__} : {time_alg_2}")
    if time_alg_2 > time_alg_1:
        print(f"{alg_1.__name__} is faster than {alg_2.__name__} by {time_alg_2 - time_alg_1}ns or {(time_alg_2 - time_alg_1) / 1e9}s")
    else:
        print(f"{alg_2.__name__} is faster than {alg_1.__name__} by {time_alg_1 - time_alg_2}ns or {(time_alg_1 - time_alg_2)/ 1e9}s")
