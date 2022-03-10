from typing_extensions import Self
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class EncryptionManager:
    def __init__(self, key):
        #key = os.urandom(32)
        nonce = os.urandom(16)
        # if (key == bytes):
        #     key = key
        # else:
        #     key = int_to_bytes(key)
        aes_context = Cipher(algorithms.AES(key),
                            modes.CTR(nonce),
                            backend=default_backend())
        self.encryptor = aes_context.encryptor()
        self.decryptor = aes_context.decryptor()

    def updateEncryptor(self, plaintext):
        return self.encryptor.update(plaintext)

    def finalizeEncryptor(self):
        return self.encryptor.finalize()

    def updateDecryptor(self, ciphertext):
        return self.decryptor.update(ciphertext)

    def finalizeDecryptor(self):
        return self.decryptor.finalize()

def int_to_bytes(i):
    i = int(i)
    return i.to_bytes(32, byteorder='big')

key = 12345678901234567890123456789012
key = int_to_bytes(key)

# #key = key.to_bytes(32, 'big') #if it doesnt work, change it to 'little'
# # Auto generate key/IV for encryption
# manager = EncryptionManager(key)

# plaintexts = [
#     b"SHORT",
#     b"MEDIUM MEDIUM MEDIUM",
#     b"LONG LONG LONG LONG LONG LONG"
# ]

# ciphertexts = []


# for m in plaintexts:
#     manager.__init__(Self)
#     ciphertexts.append(manager.updateEncryptor(m))
# ciphertexts.append(manager.finalizeEncryptor())

# for c in ciphertexts:
#     print("Recovered", manager.updateDecryptor(c))
# print("Recovered", manager.finalizeDecryptor())

# Start Auto Test
manager = EncryptionManager(key)
plaintexts = [b"validationNumber and signature",]
ciphertexts = []
recoveredtexts = []
expected = [b"validationNumber and signature",]
    
print("plaintexts: ", plaintexts)
for m in plaintexts:
    ciphertexts.append(manager.updateEncryptor(m))
ciphertexts.append(manager.finalizeEncryptor())
print("ciphertexts: ", ciphertexts)

for c in ciphertexts:
    recoveredtexts.append(manager.updateDecryptor(c))
recoveredtexts.append(manager.finalizeDecryptor())
print("recovered: ", recoveredtexts)

if expected == recoveredtexts:
    print("[PASS]")
else:
    for r_text, x_text in zip(expected, recoveredtexts):
        if r_text!=x_text:
            print("Mismatch",r_text,x_text)
    print("[FAIL]")

message = b"validationNumber and signature"
key = 12345678901234567890123456789012