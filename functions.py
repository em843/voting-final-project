

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
from tabtha_aes import *

# Public e: users all share same e but have different n values
my_e = 65537
# CLA's list of validation numbers (to be encrypted and sent to CTF)
ctfValnum = []
ctfValnum_encrypted = []

# CTF
ctf_n = 22675032247964811304377741010681025768705689936049346485778680101377361780419412229892976744577715670202551587179341582317473747052372556076228084822612474800300574464210447554115735854080872047541104271586491991401193940884347823153371229107896688630096412115433919576692709742447574583916548666951113372331515816131683709597784512003051684059499878771165735333514033053258875472338691622523281267529622600174783673495821291605920651313776635795635900964473267552884315741153907681424973048913859674207556856534666416913160161946874226983650166899194349986981105539303324539741705807370244360701173598058846718087297
ctf_d = 5603625773044815659638095936783647303812462489956134941844629795717041539827468460188086902897305079490982582448946644906141642236602620171972932264019281350468713917670207799967323159325172096403187890544498898221367121878677652986740321141210228863894311467134103811039796252325875733724650536489925266311798705229715550565137462987172371523727795446266333911997133994937800842662295597364395146595455382713122181908007116609168400495194310792084942243492003737801279279005363735843788853944718629196270074246264378176086291389509478648601161128087639912520342768368147135338477713666218082468362583131627181393601

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
    return random.randint(10000000000000000000000000000000, 99999999999999999999999999999999)

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
    encrypted_aes = simple_rsa_encrypt(user.aeskey, my_e, user.pubkey)
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
    for v in ctfValnum:
        # Add encrypted valnum to list to send to CTF
        ctfValnum_encrypted.append(simple_rsa_encrypt(v, my_e, ctf_n))
    return ctfValnum_encrypted

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
    if mister_grumble_count > madaam_goob_count:
        print(f"MISTER GRUMBLE wins with {mister_grumble_count} votes.\n")
        return 
    if mister_grumble_count < madaam_goob_count:
        print(f"MADAM GOOB wins with {madaam_goob_count} votes.\n")
        return 

# register(grimp, False)
# register(grilbo, False)
# finishRegistration()




"""

The CTF

"""

"""
Asks the user for a vote, then signs and encrypts it
"""
def vote(user):
    vote = input("Enter the number of the candidate you want to vote for: \n1. Mr. Grumble \n2. Madam Goob\n\nYour vote: ")
    while vote != "1" and vote != "2":
        print(f"Please enter a number, either 1 or 2.")
        vote = input("Enter the number of the candidate you want to vote for: \n1. Mr. Grumble \n2. Madam Goob\n")
    # Combine valnum and vote as a string (prevents attaching vote to someone else's valnum)
    combined_x = str(vote) + str(user.valnum)
    print(f"\nCombined vote and valnum: {combined_x}")
    # Sign vote + valnum with RSA
    signed_x = simple_rsa_encrypt(int(combined_x), user.privkey, user.pubkey)
    # Encrypt vote with user's aes key
    signed_x_bytes = str(signed_x).encode()
    encrypted_x = allAES(signed_x_bytes, user.aeskey)
    return int(encrypted_x) # Make encrypted vote into an int

"""
Decrypt vote + valnum and verify that user is registered
"""
def verify_vote(user, encrypted_vote):
    # Decrypt with AES
    vote_bytestring = str(encrypted_vote).encode()
    decrypted_x = allAES(vote_bytestring, user.aeskey) 
    # Unsign message
    unsigned_x = simple_rsa_decrypt(int(decrypted_x), my_e, user.pubkey)
    x_str = str(unsigned_x)
    final_vote = int(x_str[0])
    valnum = int(x_str[1:])
    # Decrypt list of valnums from CLA
    ctfValnum2 = []
    for v in ctfValnum_encrypted:
        decrypted_v = simple_rsa_decrypt(v, ctf_d, ctf_n)
        ctfValnum2.append(int(decrypted_v))
    # If user valnum is in the list, then vote is valid
    if checkValnum(valnum, ctfValnum2) == True:
        user.vote = final_vote
        print("Your vote has been counted.")
        return
    return
        

"""
Checks if the validation number sent from voter is in the list from the CLA
"""
def checkValnum(valnum, val_list):
    for v in val_list:
        if v == valnum:
            print("Validation number matches list from CLA: vote is valid")
            return
    print("Vote is invalid")
    return



register(grimp, False)

finishRegistration()

verify_vote(grimp, vote(grimp))
# TODO implement simplified for voting functions

finishVoting()
tallyVotes()