import rsa

class attackRsa:
    def __init__(self, c: int | str, public_key: tuple[int, int]):
        self.c = c
        self.n, self.e = public_key
        self.p: int
        self.q: int
        self.phi: int
        self.d: int

    def _get_pq(self) -> tuple[int, int]:
        n = self.n
        if n % 2 == 0:
            self.p, self.q = 2, n // 2
            return self.p, self.q
        
        i = 3
        while i * i <= n:
            if n % i == 0:
                self.p, self.q = i, n // i
                return self.p, self.q
            i += 2

        return None
    
    def _get_phi(self):
        self.phi = (self.p - 1) * (self.q - 1); return self.phi

    def _get_d(self):
        self.d = pow(self.e, -1, self.phi)
        return self.d
    
    def attack(self):
        pq = self._get_pq()
        if not pq: raise ValueError("failed to factor n")
        self._get_phi()
        self._get_d()

        helper = rsa.rsa()
        cracked = helper.decrypt(self.c, (self.n, self.d))
        return self.p, self.q, self.d, cracked