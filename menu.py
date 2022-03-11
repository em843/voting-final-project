"""
Authors: Tabitha Rowland, Robin Vogel, Erin Murphy, Vien Hang


Main menu where the user will choose what they want to do.


"""
from array import array
from unittest import result
from data import *
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from functions import finishVoting, tallyVotes

while True: 
    print("\nWelcome to the Goblin Voting System!")
    print("--------------------------------------- ")
    print("\nHello...")
    print("\t1. Grimp.")
    print("\t2. Gumpy.")
    print("\t3. Grimble.")   
    print("\t4. Gronk.")
    print("\t5. Grilbo.")
    print("\t6. Garth.")
    print("\t7. Gert.")
    print("\t8. Quit. \n")
    choice = input(">> ")
    print()

    # User 1
    if choice == '1':
        
        print("\nHello, Grimp. What would you like to do?")
        print("------------------------------------------- ")
        print("\t1. Register to vote.")
        print("\t2. Cast vote.")
        print("\t3. Request results.")
        print("\t4. Quit \n")
        choice = input(">> ")
        print()
        
        # Register to vote
        if choice == '1':
            
            print("Your signature number has been verified.")
            print("Your encrypted AES key has been generated.")
            print("Your decrypted AES key has been generated.")
            print("Your validation number has been generated, thank you for registering!")
            continue
            
        # Cast vote
        elif choice == '2':
            print("Your signature number has been verified!")
            print("Your encrypted AES message has been generated.")
            print("Your decrypted AES message has been generated.")
            
            # Vote
            vote()
            print("Your vote has been casted, thank you for voting!")
            continue

        elif choice == '3':
            finishVoting()
            print("All votes have been casted.")
            print("Our winner is...")
            tallyVotes()
            print("Thank you for voting in the Goblin Election!")
            continue
            
        # Quit
        elif choice == '4':
            print("Returning to main menu... \n")
            continue

        else: 
            print("Error, unknown option {}.".format(choice))


    # Waiting for finished options, just place holders
    elif choice == '2': 
        print("\nHello, Gumpy. What would you like to do?")
        break

    elif choice == '3': 
        print("\nHello, Grimble. What would you like to do?")
        break
        
    elif choice == '4': 
        print("\nHello, Gronk. What would you like to do?")
        break
        
    elif choice == '5': 
        print("\nHello, Grilbo. What would you like to do?")
        break
        
    elif choice == '6': 
        print("\nHello, Garth. What would you like to do?")
        break
        
    elif choice == '7': 
        print("\nHello, Gert. What would you like to do?")
        break
        
    elif choice == '8':
        print("Goodbye, Goblin! \n")
        break

    else:
        print("unknown option {}.".format(choice))
