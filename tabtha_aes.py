from re import I
from typing_extensions import Self
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class EncryptionManager:
    def __init__(self, key):
        nonce = os.urandom(16) #can be randomly generated everytime, only used once
        aes_context = Cipher(algorithms.AES(key), #key must be in byte form, 32 length
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

#uses all of the above functions & class
def allAES(message, key):
        key = int_to_bytes(key)
        manager = EncryptionManager(key)
        plaintexts = [message]
        ciphertexts = []
        recoveredtexts = []
        finalrecoveredtexts = []
        
        print("plaintexts: ", plaintexts)
        for m in plaintexts:
                ciphertexts.append(manager.updateEncryptor(m))
        ciphertexts.append(manager.finalizeEncryptor())
        print("ciphertexts: ", ciphertexts)

        for c in ciphertexts:
                recoveredtexts.append(manager.updateDecryptor(c))
        recoveredtexts.append(manager.finalizeDecryptor())

        print("recovered: ", recoveredtexts)
        
        for i in recoveredtexts:
            newi = i.decode()
            finalrecoveredtexts.append(newi)
        finalrecoveredtext = finalrecoveredtexts[0]

        print("finalrecoveredtext: ", finalrecoveredtext)

        return finalrecoveredtext
        


if __name__ == "__main__":

        # #variables for the test
        message = b"validationNumber and signature"
        key = 12345678901234567890123456789012

        allAES(message, key)

        # key = int_to_bytes(key)
        # manager = EncryptionManager(key)
        # plaintexts = [message]
        # ciphertexts = []
        # recoveredtexts = []
        # expected = [message, b'', b''] #when it passes through the updateEncryptor or updateDecryptor, an empty byte sstring b' ' gets added. dont know how to avoid this.
        
        # print("plaintexts: ", plaintexts)
        # for m in plaintexts:
        #         ciphertexts.append(manager.updateEncryptor(m))
        # ciphertexts.append(manager.finalizeEncryptor())
        # print("ciphertexts: ", ciphertexts)

        # for c in ciphertexts:
        #         recoveredtexts.append(manager.updateDecryptor(c))
        # recoveredtexts.append(manager.finalizeDecryptor())

        # print("recovered: ", recoveredtexts)
        # print("expected: ", expected)

        # finalrecoveredtexts = []

        # for i in recoveredtexts:
        #     newi = i.decode()
        #     finalrecoveredtexts.append(newi)
        # finalrecoveredtext = finalrecoveredtexts[0]

        # print("finalrecoveredtext: ", finalrecoveredtext)
       

        # if expected == recoveredtexts:
        #         print("[PASS]")
        # else:
        #         for r_text, x_text in zip(expected, recoveredtexts):
        #                 if r_text!=x_text:
        #                         print("Mismatch",r_text,x_text)
        #         print("[FAIL]")


        