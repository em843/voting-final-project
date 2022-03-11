"""
Authors: Tabitha Rowland, Robin Vogel, Erin Murphy, Vien Hang



Each person has their own public and private key
We create a secret to send them, encrypt it with the public key, and they can decrypt it with their private key


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
         print("\nHello, choose a goblin to register to vote")
         print("\nWhen finished chose vote and you will be taken to the next step")
         print("\t1. Grimp.")
         print("\t2. Gumpy.")
         print("\t3. Grimble.")   
         print("\t4. Gronk.")
         print("\t5. Grilbo.")
         print("\t6. Garth.")
         print("\t7. Gert.")
         print("\t8. Vote. \n")
         print("\t9. Quit. \n")
         choice = input(">> ")
         print()

         if choice == '1':
               
               print("\nHello, Grimp.")
               print("Here is your signature number:")
               print("Your signature number has been verified!")
               print("Here is your encrypted AES key:")
               print("Here is your decrypted AES key:")
               print("Your validation number has been generated, thank you for registering!")
         
         if choice == '2':
               
               print("\nHello, Gumpy.")
               print("Here is your signature number:")
               print("Your signature number has been verified!")
               print("Here is your encrypted AES key:")
               print("Here is your decrypted AES key:")
               print("Your validation number has been generated, thank you for registering!")
         
         if choice == '3':
               
               print("\nHello, Grimble.")
               print("Here is your signature number:")
               print("Your signature number has been verified!")
               print("Here is your encrypted AES key:")
               print("Here is your decrypted AES key:")
               print("Your validation number has been generated, thank you for registering!")
         
         if choice == '4':
               
               print("\nHello, Gronk.")
               print("Here is your signature number:")
               print("Your signature number has been verified!")
               print("Here is your encrypted AES key:")
               print("Here is your decrypted AES key:")
               print("Your validation number has been generated, thank you for registering!")
         
         if choice == '5':
               
               print("\nHello, Grilbo.")
               print("Here is your signature number:")
               print("Your signature number has been verified!")
               print("Here is your encrypted AES key:")
               print("Here is your decrypted AES key:")
               print("Your validation number has been generated, thank you for registering!")
         
         if choice == '6':
               
               print("\nHello, Garth.")
               print("Here is your signature number:")
               print("Your signature number has been verified!")
               print("Here is your encrypted AES key:")
               print("Here is your decrypted AES key:")
               print("Your validation number has been generated, thank you for registering!")
         
         if choice == '7':
               
               print("\nHello, Gert.")
               print("Here is your signature number:")
               print("Your signature number has been verified!")
               print("Here is your encrypted AES key:")
               print("Here is your decrypted AES key:")
               print("Your validation number has been generated, thank you for registering!")
         
         if choice == '8':

               finishRegistration()
               print("\nAll other goblins selected have been automatically registered to vote")
               print("\nWelcome to the Voting section! Choose a goblin to vote")
               print("\t1. Grimp.")
               print("\t2. Gumpy.")
               print("\t3. Grimble.")   
               print("\t4. Gronk.")
               print("\t5. Grilbo.")
               print("\t6. Garth.")
               print("\t7. Gert.")
               print("\t8. Run Election.")
               print("\t9. Quit.")
               choice = input(">> ")
               print()

               if choice == '1':
               
                     print("\nHello, Grimp.")
                     print("\nWho is your vote?")
                     print("\t1. Mister Grumble.")
                     print("\t2. Madaam Goob.")
                     choice = input(">> ")
                     print()

                     if choice == '1':
                        print()

                     if choice == '2':
                        print()

                     else: 
                        print("Error, unknown option {}.".format(choice))

               if choice == '2':
               
                     print("\nHello, Gumpy.")
                     print("\t1. Mister Grumble.")
                     print("\t2. Madaam Goob.")
                     choice = input(">> ")
                     print()
         
               if choice == '3':
               
                     print("\nHello, Grimble.")
                     print("\t1. Mister Grumble.")
                     print("\t2. Madaam Goob.")
                     choice = input(">> ")
                     print()
         
               if choice == '4':
               
                     print("\nHello, Gronk.")
                     print("\t1. Mister Grumble.")
                     print("\t2. Madaam Goob.")
                     choice = input(">> ")
                     print()
         
               if choice == '5':
            
                     print("\nHello, Grilbo.")
                     print("\t1. Mister Grumble.")
                     print("\t2. Madaam Goob.")
                     choice = input(">> ")
                     print()
         
               if choice == '6':
               
                     print("\nHello, Garth.")
                     print("\t1. Mister Grumble.")
                     print("\t2. Madaam Goob.")
                     choice = input(">> ")
                     print()
         
               if choice == '7':
               
                     print("\nHello, Gert.")
                     print("\t1. Mister Grumble.")
                     print("\t2. Madaam Goob.")
                     choice = input(">> ")
                     print()

               if choice == '8':
               
                     finishVoting()
                     print("\nTallying up the Goblins results.")
                     result = tallyVotes()
                     print("\nThe winner of the Election is")
                     print("\n*Cue drumroll*")
                     print(result)

                     print("Thank you for voting in the Goblin Election.")
                  

               if choice == '9':
                  print("Goodbye, Goblin! \n")
                  break
               
               else: 
                     print("Error, unknown option {}.".format(choice))

         if choice == '9':
            print("Goodbye, Goblin! \n")
            break
         
         else: 
            print("Error, unknown option {}.".format(choice))