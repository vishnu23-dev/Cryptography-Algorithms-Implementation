def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char

    return result

message = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(message, shift)

print("Encrypted Text:", encrypted)
