import rsa
import attack

demo = rsa.rsa()
n, e, _ = demo.gen_keypair()
print(f"Keypair: {(n, e, _)}")
message = input("Enter the message: ")
cipher = demo.encrypt(message, [n, e])
print(f"Encrypted: {cipher}\nPublic Key: {(n, e)}")

attack = attack.attackRsa(cipher, (n, e))
p, q, d, cracked = attack.attack()
print(f"""Factored n into p={p}, q={q}
Recovered private exponent d={d}
Decrypted message: {cracked}""")