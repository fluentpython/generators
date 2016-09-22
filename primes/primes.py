#!/usr/bin/env python3

from array import array

TYPECODE = 'Q'  # 64-bit unsigned integer
THRESHOLD = 2**64

def primes():
    """Prime number generator"""

    yield 2
    seen = array(TYPECODE)
    candidate = 3

    while True:
        is_prime = True

        for n in seen:
            if candidate % n == 0:
                is_prime = False
                break
            if n * n > candidate:
                break

        if is_prime:
            yield candidate
            seen.append(candidate)  # OverflowError if candidate >= 2**64

        candidate += 2


if __name__ == '__main__':

    import sys
    try:
        num_primes = int(sys.argv[-1])
    except ValueError:
        print('Usage: {} <how_many_primes>'.format(sys.argv[0]))
        print('\t' + primes.__doc__)
        sys.exit(-1)

    for _, p in zip(range(num_primes), primes()):
        print('{:,}'.format(p), end=' ')

    print()
