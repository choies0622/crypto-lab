import rsa

demo = rsa.rsa()
n, e, d = demo.gen_keypair()
print(f"Keypair: {(n, e, d)}")

message = input("Enter the message: ")

cipher = demo.encrypt(message, [n, e])
decrypted = demo.decrypt(cipher, [n, d])
print(f"Encrypted: {cipher}")
print(f"Decrypted: {decrypted}")