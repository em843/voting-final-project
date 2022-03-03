

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


"""
Register to vote
"""
def register(user):
    validation_number[user] = get_validation()
    # Encrypt 
    priv_key[user]
    return


def get_validation():
    return 12345

def generate_aes():
    return




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

