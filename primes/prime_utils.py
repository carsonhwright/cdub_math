from math import sqrt


def get_primes_less_than(n):
    """This is not optimized, be careful
    """
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