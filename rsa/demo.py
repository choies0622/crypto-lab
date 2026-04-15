import rsa

demo = rsa.rsa()
print(f"Keypair: {demo.gen_keypair()}")

message = input("Enter the message: ")

encrypted = demo.encrypt(message)
decrypted = demo.decrypt(encrypted)
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")