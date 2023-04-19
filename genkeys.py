#! /usr/bin/env python3
import sys
import math

from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Math.Numbers import Integer
from dataclasses import dataclass
from decimal import Decimal
from secrets import SystemRandom
from random import randrange
from rsa import generate

def miller_rabin (n, k=40):
    print("Execute miller_rabin!")
    
    def is_composite(a, d, n, s):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(1, s):
            x = pow(x, 2, n)
            if x == n - 1:               
                return False
    return True # n is composite

    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
              61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
              131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
              197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269,
              271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
              353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431,
              433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
              509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
              601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673,
              677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761,
              769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857,
              859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947,
              953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031,
              1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097,
              1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187,
              1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277,
              1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327,
              1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439,
              1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499,
              1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583,
              1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663,
              1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747,
              1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847,
              1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931,
              1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011)
    if n < 2017:
        return n in primes
    if any(not n % x for x in primes):
        return False
    
    # Decompose (n - 1) to write it as (2 ** s) * d
    d = n - 1
    s = 0
    while not d & 1:    # while d % 2 == 0
        d >>= 1         # d = d // 2
        s += 1

    # Smallest odd numbers for which Miller-Rabin primality test on bases <= n-th prime 
    bases = (2047, 1373653, 25326001, 3215031751, 2152302898747,
             3474749660383, 341550071728321, 341550071728321,
             3825123056546413051, 3825123056546413051,
             3825123056546413051, 318665857834031151167461,
             3317044064679887385961981)
    for i, base in enumerate(bases, 1):
        if n < base:            
            return not any(is_composite(a, d, n, s) for a in primes[:i])
    return not any(is_composite(randrange(2, n-1), d, n, s) for a in range(k))

def getprime(bits: int, e=65537):
    # Generate a random bits size prime number
    print("Execute getprime")
    
    secure_randrange = SystemRandom().randrange
    
    #  Prime shall be (lowlimit < p < 2**bits-1).
    lowlimit = int(Decimal(2**0.5) * Decimal(2**(bits - 1)))
    lowlimit |= 1 # n += 1 if n is odd
    highlimit = 2**bits    
    while True:
        p = secure_randrange(lowlimit, highlimit, 2)
        
        # (p–1) shall be relatively prime to e. FIPS 186-4. B.3.1
        if math.gcd(e, p - 1) == 1:            
            if miller_rabin(p):
                return p
@dataclass
#**************************
class RsaKey:
    tag="RSA-####"
    p:int = 0
    q:int = 0
    e:int = 0
    d:int = 0
    n:int = 0

    def __init__(self, n, e, d, p, q):
        self.e=e
        self.d=d
        self.n=n
        self.p=p
        self.q=q

    def create(self, n, e, d, p, q):
        self.e=Integer(e)
        self.d=Integer(d)
        self.n=Integer(n)
        self.p=Integer(p)
        self.q=Integer(q)
        return self

    # Use this routine to generate the RSA TEST Key    
    def generate_key(self, bits, e=65537):
        key = generate (bits, e=e)
        return self.create(n=key[0], e=key[1], d=key[2], p = key[3], q=key[4])

    def Generate(self, nlen, e=65537):
        print("Begin generate keys")

        # Get public and private keys.
        bits = nlen//2
        # First factor of n (p).
        p = getprime(bits)
        while True:
            # Second factor of n (q)
            q = getprime(bits)
            
            # FIPS 186-4. B.3.1
            if abs(p - q) > 2**(bits-100):

                # Euler's function phi.
                phi = (p - 1) * (q - 1)

                # If greatest common denominator(gcd)(x,y) = 1, x and y are relatively prime
                if math.gcd(e, phi) == 1:
                    n = p * q
                    
                    # Private (or decryption) exponent d
                    d = pow(e, -1, phi)
                    
                    # If phi ≤ d ≤ 2**(nlen//2), new p, q, d shall be determined.
                    if 2**bits < d < phi:
                        # print("Public key is ",(E, n))
                        # print("Private key is", (d, n))
                        key = self.create(p=p, q=q, n=n, d=d, e=e)
                        return key


    def public_key(self):
        return (self.n, self.e)

    def private_key(self):
        return (self.n, self.d)

    def writekey (self, f, public=True):
        e=long_to_bytes(self.e)
        d=long_to_bytes(self.d)
        n=long_to_bytes(self.n)
        p=long_to_bytes(self.p)
        q=long_to_bytes(self.q)
        
        if public:
            f.write(b'1')
        else:
            f.write(b'0')
        f.write(e)
        f.write(d)
        f.write(n)
        f.write(p)
        f.write(q)

    def readkey (self, f):
        starttag=0
        tagsize=1
        starte = starttag+tagsize
        esize=3
        startd = starte+esize
        dsize=128
        startn= startd+dsize
        nsize=128
        startp=startn+nsize
        psize=64
        startq=startp+psize
        qsize=64
        end=startq+qsize

        data=f.read()
        datasize = len(data)
        if datasize != end:
            print ("readkey sizes are not equal!", datasize, "!=", end)

        tag = data[starttag:starte]
        if tag==b'1':
            print ("Public Key")
            self.e = Integer(bytes_to_long(data[starte:startd]))
            # self.d = Integer(bytes_to_long(data[startd:startn]))
            self.n = Integer(bytes_to_long(data[startn:startp]))
            # self.p = Integer(bytes_to_long(data[startp:startq]))
            # self.q = Integer(bytes_to_long(data[startq:end]))

        else:
            self.e = Integer(bytes_to_long(data[starte:startd]))
            self.d = Integer(bytes_to_long(data[startd:startn]))
            self.n = Integer(bytes_to_long(data[startn:startp]))
            self.p = Integer(bytes_to_long(data[startp:startq]))
            self.q = Integer(bytes_to_long(data[startq:end]))
       

    def encrypt(self, plaintext):
        if not 0 <= plaintext < self.n:
            raise ValueError("Plaintext too large")
        if self.e == Integer(0):
            raise ValueError ("Not a valid key")
        return int(pow(Integer(plaintext), self.e, self.n))

    def decrypt(self, ciphertext):
        u=dp=dq=Integer(0)
        if not 0 <= ciphertext < self.n:
            raise ValueError("Ciphertext too large")
        if self.d == Integer(0):
            raise ValueError ("Not a valid key")
        dp = self.d % (self.p - 1)
        dq = self.d % (self.q - 1)
        u = self.p.inverse(self.q)
        r=Integer(1)
        cp = Integer(ciphertext) * pow(r, self.e, self.n) % self.n
        m1 = pow(cp, dp, self.p)
        m2 = pow(cp, dq, self.q)
        h = ((m2 - m1) * u) % self.q
        mp = h * self.p + m1
        result = (r.inverse(self.n) * mp) % self.n

        # Verify no faults occurred
        if ciphertext != int(pow(Integer(result), self.e, self.n)):
            print("ERROR in RSA DECRYPTION")
            # print ("Ciphertext",ciphertext, "not equal")
            # print(pow(result, self.e, self.n))
            # print("e", self.e, type(self.e))
            # print("n", self.n, type(self.n))
        return result

def main():
    print ("GEN RSA KEYS MAIN")
    if (len(sys.argv)) !=2:
        raise ValueError("Missing user name!")
    username = sys.argv[1]

    print("Input:", username)

    rkey=RsaKey(p=0,q=0,n=0,d=0,e=65537)    
    rkey.generate_key(bits=1024, e=65537)    
    print ("Generated Key\n", rkey)

    # write keys to a file
    f = open(username+".prv","wb")
    rkey.writekey(f=f,public=False)
    f = open(username+".pub","wb")
    rkey.writekey(f=f,public=True)
    f.close()
    print ("Write keys",username+".pub", username+".prv")

    plain = 11234567890123456
    # encryption/decryption check
    encrypted=rkey.encrypt(plain)
    # print ("Encrypted text", encrypted)

    try:
        decrypted=rkey.decrypt (encrypted)
        if plain != decrypted:
            print ("RSA DECRYPTION TEST FAILED")
    except ValueError:
        print ("RSA DECRYPTION FAILURE, ValueError")

    publickey=RsaKey(p=rkey.p,q=rkey.q,n=0,d=0,e=0)
    # read back public key data
    print ("Read keys",username)
    f=open(username+".pub","rb")
    publickey.readkey(f)
    f.close()

    privatekey=RsaKey(p=rkey.p,q=rkey.q,n=0,d=0,e=65537)
    # read back private key data
    f=open(username+".prv","rb")
    privatekey.readkey(f)
    f.close()

    # encryption/decryption check
    plain=1234567890123456
    encrypted=publickey.encrypt(plain)
    print ("RSA PUBLIC KEY ENCRYPTION TEST PASSED")
    try:
        decrypted=privatekey.decrypt(encrypted)
        if plain != decrypted:
            print ("RSA PRIVATE KEY DECRYPTION TEST FAILED")
    except ValueError:
        print ("RSA DECRYPTION FAILURE, ValueError")

    try:
        decrypted=publickey.decrypt(encrypted)
        print ("RSA PUBLIC KEY DECRYPTION TEST FAILED")
    except ValueError:
        print ("RSA PUBLIC KEY DECRYPTION TEST PASSED")
  

    print ("GEN RSA KEYS COMPLETE")
        
if __name__ == "__main__":
    main()
