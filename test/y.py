import hashlib

with open("1.txt", "r") as file:
    encrypted_data = hashlib.sha512(file.read().encode())
    print(encrypted_data.hexdigest())
