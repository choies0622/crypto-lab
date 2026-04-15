# import rsa
import random as r
import math as m
# instead of using existing RSA library, I will implement RSA algorithm using the following steps:
# 1. Generate a prime number p
# 2. Generate a prime number q
# 3. Calculate n = p * q
# 4. Calculate phi = (p - 1) * (q - 1)
# 5. Choose an integer e such that 1 < e < phi and gcd(e, phi) = 1
# 6. Calculate d such that d * e ≡ 1 (mod phi)
# 7. The public key is (n, e) and the private key is (n, d)
# 8. To encrypt a message m, calculate c = m^e mod n
# 9. To decrypt a message c, calculate m = c^d mod n

class rsa:
    def __init__(self, p: int = None, q: int = None):
        self.prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        self.p = p
        self.q = q
        self.n: int
        self.phi: int
        self.e: int
        self.d: int

    def is_prime(self, n):
        if n in self.prime: return True
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        self.prime.add(n)
        return True

    def _gen_prime(self):
        while True:
            p = r.randint(2, 1000)
            if self.is_prime(p):
                return p
    
    def _gen_e(self):
        while True:
            e = r.randint(2, self.phi - 1)
            if m.gcd(e, self.phi) == 1:
                return e
    def _gen_d(self):
        while True:
            d = r.randint(2, self.phi - 1)
            if d * self.e % self.phi == 1:
                return d

    def gen_keypair(self) -> tuple[int, int, int]:
        if self.p is None: self.p = self._gen_prime()
        if self.q is None: self.q = self._gen_prime()
        while self.p == self.q: self.q = self._gen_prime()
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self._gen_e()
        self.d = self._gen_d()
        return self.n, self.e, self.d

    def encrypt(self, m: int | str, public_key: tuple[int, int]) -> tuple:
        n, e = public_key
        m = [ord(char) for char in m]
        r = []
        for i in range(len(m)):
            r.append(pow(m[i], e, n))
        return r

    def decrypt(self, c: tuple, private_key: tuple[int, int]) -> int | str:
        n, d = private_key
        r = []
        for i in range(len(c)):
            r.append(chr(pow(c[i], d, n)))
        r = "".join(r)
        return r