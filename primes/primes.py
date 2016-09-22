#!/usr/bin/env python3

from array import array

TYPECODE = 'Q'  # 64-bit unsigned integer


def primes():
    """yield primes; stop at first prime after 2**64"""
    yield 2
    seen = array(TYPECODE)
    candidate = 3

    while True:
        factor = None

        for n in seen:
            if candidate % n == 0:
                factor = n
                break
            if n * n > candidate:
                break

        if factor is None:
            yield candidate
            try:
                seen.append(candidate)
            except OverflowError:
                return

        candidate += 2


if __name__ == '__main__':

    import sys
    try:
        num_primes = int(sys.argv[-1])
    except ValueError:
        print('Usage: {} <how_many_primes>'.format(sys.argv[0]))
        sys.exit(-1)

    for _, p in zip(range(num_primes), primes()):
        print(p)
