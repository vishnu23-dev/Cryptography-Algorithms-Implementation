import hashlib

text = input("Enter text: ")

hash_value = hashlib.sha256(text.encode()).hexdigest()

print("\nSHA256 Hash:")
print(hash_value)
