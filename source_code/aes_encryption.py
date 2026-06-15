from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

key = b'1234567890123456'

message = input("Enter message: ")

cipher = AES.new(key, AES.MODE_ECB)

encrypted = cipher.encrypt(
    pad(message.encode(), AES.block_size)
)

encrypted_text = base64.b64encode(encrypted).decode()

print("\nEncrypted Text:")
print(encrypted_text)

decrypted = unpad(
    cipher.decrypt(base64.b64decode(encrypted_text)),
    AES.block_size
)

print("\nDecrypted Text:")
print(decrypted.decode())
