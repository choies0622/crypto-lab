class caeser:
    def encrypt(self, m: str, key: int):
        m = m.upper()
        encrypted = []
        for char in m:
            if char.isupper():
                encrypted.append(chr((ord(char) - ord('A') + int(key)) % 26 + ord('A')))
            elif char.isdigit():
                encrypted.append(chr((ord(char) - ord('0') + int(key)) % 10 + ord('0')))
            else: encrypted.append(char)
        encrypted = "".join(encrypted)
        return encrypted

    def decrypt(self, c: str, key: int):
        c = c.upper()
        decrypted = []
        for char in c:
            if char.isupper():
                decrypted.append(chr((ord(char) - ord('A') - int(key)) % 26 + ord('A')))
            elif char.isdigit():
                decrypted.append(chr((ord(char) - ord('0') - int(key)) % 10 + ord('0')))
            else: decrypted.append(char)
        decrypted = "".join(decrypted)
        return decrypted