"""
Authors: Tabitha Rowland, Robin Vogel, Erin Murphy, Vien Hang


Main menu where each individual user will vote for a candidate.
Each person has their own public and private key.
We create a secret to send them, encrypt it with the public key, and they 
can decrypt it with their private key

"""
from array import array
from unittest import result
from data import *
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from functions import *

if __name__ == "__main__":

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
            
                # Register to vote
                if choice == '1':
                    register(grimp, False)
                    print("Thank you for registering!")
                    print("\t1. Return.")
                    choice = input(">> ")
                    print()

                    if choice == '1':
                        continue
                    else: 
                        print("Error, unknown option {}.".format(choice))
                        break
                        
                # Cast vote
                elif choice == '2':
                    verify_vote(grimp, vote(grimp))
                    print("\t1. Return.")
                    choice = input(">> ")
                    print()

                    if choice == '1':
                        continue
                    else: 
                        print("Error, unknown option {}.".format(choice))
    
                # Request results
                elif choice == '3':
                    print("All votes have been counted.")
                    finishVoting()
                    tallyVotes()
                    print("Thank you for voting in the Goblin Election!")
                    break
                    
                # Quit
                elif choice == '4':
                    print("Returning to main menu... \n")
                    break
    
                else: 
                    print("Error, unknown option{}.".format(choice))
                    
            # User 2
            elif choice == '2': 
                print("\nHello, Gumpy. What would you like to do?")
                print("------------------------------------------- ")
                print("\t1. Register to vote.")
                print("\t2. Cast vote.")
                print("\t3. Request results.")
                print("\t4. Quit \n")
                choice = input(">> ")
        
            # User 3
            elif choice == '3': 
                print("\nHello, Grimble. What would you like to do?")
                print("------------------------------------------- ")
                print("\t1. Register to vote.")
                print("\t2. Cast vote.")
                print("\t3. Request results.")
                print("\t4. Quit \n")
                choice = input(">> ")
            
            # User 4
            elif choice == '4': 
                print("\nHello, Gronk. What would you like to do?")
                print("------------------------------------------- ")
                print("\t1. Register to vote.")
                print("\t2. Cast vote.")
                print("\t3. Request results.")
                print("\t4. Quit \n")
                choice = input(">> ")
            
            # User 5
            elif choice == '5': 
                print("\nHello, Grilbo. What would you like to do?")
                print("------------------------------------------- ")
                print("\t1. Register to vote.")
                print("\t2. Cast vote.")
                print("\t3. Request results.")
                print("\t4. Quit \n")
                choice = input(">> ")
            
            # User 6
            elif choice == '6': 
                print("\nHello, Garth. What would you like to do?")
                print("------------------------------------------- ")
                print("\t1. Register to vote.")
                print("\t2. Cast vote.")
                print("\t3. Request results.")
                print("\t4. Quit \n")
                choice = input(">> ")
            
            # User 7
            elif choice == '7': 
                print("\nHello, Gert. What would you like to do?")
                print("------------------------------------------- ")
                print("\t1. Register to vote.")
                print("\t2. Cast vote.")
                print("\t3. Request results.")
                print("\t4. Quit \n")
                choice = input(">> ")
            
            # Quit main menu
            elif choice == '8':
                print("Goodbye, Goblin! \n")
                break
        
            else:
                print("unknown option {}.".format(choice))