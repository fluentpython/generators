import zipfile
import lzma

from array import array

TYPECODE = 'L'  # unsigned 32-bit long

primes = array('L')

with zipfile.ZipFile('primes1.zip') as inzip:
    with inzip.open('primes1.txt') as infile:
        next(infile), next(infile)  # skip first 2 lines
        for lin in infile:
            fields = lin.split()
            for field in fields:
                primes.append(int(field))

with lzma.open('primes1.xz', 'wb') as outfile:
    primes.tofile(outfile)
