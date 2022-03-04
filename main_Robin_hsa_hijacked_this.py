"""
Authors: Tabitha Rowland, Robin Vogel, Erin Murphy, Vien Hang



Each person has their own public and private key
We create a secret to send them, encrypt it with the public key, and they can decrypt it with their private key


"""
from array import array
from data import *
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa


 # import modules


# List of eligible voters: [user, privateKey, publicKey]
    # in theory, CLA does not have privateKey


# User sends registration number (secret)

# Generate an AES key for a user
# 
# Encrypt with user's public key


# Eligible voter signs up
# They have a private key and their public key is known by CLA
# CLA gets a number for them, encrypts it with their public key and sends to user
    # also sends an AES key (encrypted with public key)





# Votes themselves should be numbers (easiest)
    # Should be signed (ecnrypt with privatek ey)
    # Then encrypt that with AES key and send to CTF



def generateKeys():
    for i in range(7):
        private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend())
        keys.append(keys)
    return keys

def printKeys(keys):
    for x in keys:
        private_key_temp = keys(x)
        print(private_key_temp.private_numbers().d)

if __name__ == "__main__":
    keys = []
    
    for i in range(7):
        private_key = rsa.generate_private_key(   
            public_exponent=65537,
            key_size=2048,
            backend=default_backend())
        print(private_key.private_numbers().d)
        keys.append(keys)
    for x in keys:
        private_key = keys.index(x)
        print(private_key.private_numbers().d)