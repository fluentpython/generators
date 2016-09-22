import lzma

from array import array

TYPECODE = 'L'  # unsigned 32-bit long

primes = array('L')

with lzma.open('primes1.xz', 'rb') as infile:
    primes.fromfile(infile, 10**6)

assert len(primes) == 1000000
assert primes[0] == 2
assert primes[-1] == 15485863

print(len(primes), 'smallest primes: from', primes[0], 'to', primes[-1])
