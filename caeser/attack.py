import caeser

class attackCaeser():
    def attack(self, m: str):
        m = m.upper()
        final = []
        for key in range(26):
            cracked = []
            for char in m:
                if char.isupper():
                    cracked.append(chr((ord(char) - ord('A') - int(key)) % 26 + ord('A')))
                elif char.isdigit():
                    cracked.append(chr((ord(char) - ord('0') - int(key)) % 10 + ord('0')))
                else: cracked.append(char)
            cracked = "".join(cracked)
            final.append(cracked)
        return final