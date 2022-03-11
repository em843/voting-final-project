

"""
Each voter will send a message to the CLA asking for a validation number, 
and CLA will return a random validation number. The CLA retains a list of 
validation numbers as well as a list of validation numbers' recipients to prevent a 
voter from voting twice. Then, the CLA completes its task by sending the list of 
validation number to the CTF. CTF's main function is to count votes. CTF checks the 
validation number against the list received from the CLA. If the validation number 
is there, the CTF crosses it off (to prevent someone from voting twice). The CTF 
adds the validation number to the list of people who voted for a particular 
candidate and adds one to the tally. After all the votes have been received, 
the CTF publishes the outcome.
"""
from data import *
import gmpy2
from cryptography.hazmat.primitives.asymmetric import rsa
import random
import os
import sys
from ctf import ctf_n

# Public e: users all share same e but have different n values
my_e = 65537
# CLA's list of validation numbers (to be encrypted and sent to CTF)
ctfValnum = []

# Encrypts a numerical plaintext with RSA
def simple_rsa_encrypt(x, e, n):
    return gmpy2.powmod(x, e, n)

# Encrypts a numerical plaintext with RSA
def simple_rsa_decrypt(y, d, n):
    return gmpy2.powmod(y, d, n)

# Validates a signature
def check_signature(x, d, e, n):
    y = simple_rsa_encrypt(x, d, n)
    print("Your message has been signed")
    plaintext = simple_rsa_decrypt(y, e, n)
    if x == plaintext:
        return True
    else: 
        return False

"""
Generates a random validation number for a voter
"""
def get_validation():
    return random.randint(1000000000, 9999999999)

"""
Generates a random aes key
"""
def get_aes():
    return os.urandom(32)

"""
Register to vote
Params:
user: the user to be registered
simplified: if the statements are to be printed
"""
def register(user, simplified):
    print(f"Hello, {user.name}.")
    print(f"Your public registration number: {user.regnum}")
    # Identity check (checks validity of pub and priv keys)
    if check_signature(user.regnum, user.privkey, my_e, user.pubkey): 
        # Check if already registered
        if user.valnum != 0:
            print("Already registered.")
            return
        # Generate validation number and aes key
        user.valnum = get_validation()
        ctfValnum.append(user.valnum)
        user.aeskey = get_aes()
        print("Identity check passed. Validation number generated.")
    else:
        print("Identity check failed. Voter ineligible.")
        return
    # Encrypt validation number with user's public key
    encrypted_vn = simple_rsa_encrypt(user.valnum, my_e, user.pubkey)
    # Encrypt new AES key with user's public key
    aesint = int.from_bytes(user.aeskey, sys.byteorder) # convert aeskey bytes to int
    encrypted_aes = simple_rsa_encrypt(aesint, my_e, user.pubkey)
    # Decrypt validation number with user's priv key
    decrypted_vn = simple_rsa_decrypt(encrypted_vn, user.privkey, user.pubkey)
    # Decrypt AES key with user's priv key
    decrypted_aes = simple_rsa_decrypt(encrypted_aes, user.privkey, user.pubkey)

    if simplified == False:
        print(f"Encrypted validation number: {encrypted_vn}")
        print(f"Encrypted AES key: {encrypted_aes}")
        print(f"Decrypted validation number: {decrypted_vn}")
        print(f"Decrypted AES key: {decrypted_aes}")
    return 


"""
This function finishes the registration step by registering all the 
unregistered users and finally sending the encrypted validation numbers
to CTF.
"""
def finishRegistration():
    register_count = 0
# Register all unregistered users
    for user in user_master_list:
        if user.valnum == 0:
            register(user, True)
            register_count+=1
    print(f"{register_count} users registered.")

# Encrypt each item in ctfValnum with the CTF pub key and send it to CTF
    ctfValnum_encrypted = []
    for v in ctfValnum:
        # Add encrypted valnum to list to send to CTF
        ctfValnum_encrypted.append(simple_rsa_encrypt(v, my_e, ctf_n))
    return 

def finishVoting():
    voter_count = 0
# Votes for all users who haven't voted
    for user in user_master_list:
        if user.vote == 0:
            user.vote = random.randint(1, 2)
            voter_count += 1
    print(f"{voter_count} users voted for")

def tallyVotes():
    mister_grumble_count = 0
    madaam_goob_count = 0
    for user in user_master_list:
        if user.vote == 1:
            mister_grumble_count += 1
        if user.vote == 2:
            madaam_goob_count += 1
    if mister_grumble_count < madaam_goob_count:
        return "MISTER GRUMBLE"
    if mister_grumble_count > madaam_goob_count:
        return "MADAAM GOOB"

# register(grimp, False)
# register(grilbo, False)
# finishRegistration()