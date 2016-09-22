import sys
import lzma
from array import array

from primes import primes

TYPECODE = 'L'  # unsigned 32-bit long

try:
    num_primes = int(sys.argv[-1])
except ValueError:
    print('Usage: {} <how_many_primes>'.format(sys.argv[0]))
    sys.exit(-1)

fixture = array('L')

with lzma.open('primes1.xz', 'rb') as infile:
    fixture.fromfile(infile, 10**6)


num_primes = min(num_primes, len(fixture))

for _, a, b in zip(range(num_primes), primes(), fixture):
    assert a == b

print('{:,} primes OK'.format(num_primes))
