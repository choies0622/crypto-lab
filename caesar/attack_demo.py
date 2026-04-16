import caesar
import attack

demo = caesar.caesar()

message = input("Enter the message [str & int]: ")
key = input("Enter the key [int]: ")
cipher = demo.encrypt(message, key)
print(f"Encrypted: {cipher}")

attack = attack.attackcaesar()
cracked = "\n".join(attack.attack(cipher))
print(f"Decrypt trial:\n{cracked}")