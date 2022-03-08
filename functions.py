

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


my_e = 65537

def simple_rsa_encrypt(x, e, n):
    return gmpy2.powmod(x, e, n)

def simple_rsa_decrypt(y, d, n):
    return gmpy2.powmod(y, d, n)

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
    return 12345

def get_aes():
    # TODO: Implement this
    return 1234567890

"""
Register to vote
"""
def register(user):
    print(f"Your public registration number: {user.regnum}")
    # Check if already registered
    if user.valnum != 0:
        print("Already registered.")
        return
    # Identity check (checks validity of pub and priv keys)
    if check_signature(user.regnum, user.privkey, my_e, user.pubkey): 
        user.valnum = get_validation()
        print("Voter is eligible. Validation number generated.")
    # Encrypt validation number with user's public key
    encrypted_vn = simple_rsa_encrypt(user.valnum, my_e, user.pubkey)
    print(f"Encrypted validation number: {encrypted_vn}")
    # Encrypt new AES key with user's public key
    encrypted_aes = simple_rsa_encrypt(get_aes(), my_e, user.pubkey)
    print(f"Encrypted AES key: {encrypted_aes}")
    # Decrypt validation number with user's priv key
    decrypted_vn = simple_rsa_decrypt(encrypted_vn, user.privkey, user.pubkey)
    print(f"Decrypted validation number: {decrypted_vn}")
    # Decrypt AES key with user's priv key
    decrypted_aes = simple_rsa_decrypt(encrypted_aes, user.privkey, user.pubkey)
    print(f"Decrypted AES key: {decrypted_aes}")
    return 


register(grimp)






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



user = grimp
#user_privkey[user]

