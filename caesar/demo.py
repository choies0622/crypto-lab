import caeser

demo = caeser.caeser()

message = input("Enter the message [str & int]: ")
key = input("Enter the key [int]: ")

cipher = demo.encrypt(message, key)
decrypted = demo.decrypt(cipher, key)
print(f"Encrypted: {cipher}")
print(f"Decrypted: {decrypted}")