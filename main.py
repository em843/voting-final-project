"""
Authors: Tabitha Rowland, Robin Vogel, Erin Murphy, Vien Hang



Each person has their own public and private key
We create a secret to send them, encrypt it with the public key, and they can decrypt it with their private key


"""
from data import *


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



user = "grumble"
user_privkey[user]

