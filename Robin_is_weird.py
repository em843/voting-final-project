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
               
               register(grimp)
               print("\t1. Return.")
               choice = input(">> ")
               print()

               if choice == '1':
                     break
               else: 
                     print("Error, unknown option {}.".format(choice))
         
         elif choice == '2':
               
               register(gumpy)
               print("\t1. Return.")
               choice = input(">> ")
               print()

               if choice == '1':
                     break
               else: 
                     print("Error, unknown option {}.".format(choice))
         
         elif choice == '3':
               
               register(grimble)
               print("\t1. Return.")
               choice = input(">> ")
               print()

               if choice == '1':
                     break
               else: 
                     print("Error, unknown option {}.".format(choice))
         
         elif choice == '4':
               
               register(gronk)
               print("\t1. Return.")
               choice = input(">> ")
               print()

               if choice == '1':
                     break
               else: 
                     print("Error, unknown option {}.".format(choice))
         
         elif choice == '5':
               
               register(grilbo)
               print("\t1. Return.")
               choice = input(">> ")
               print()

               if choice == '1':
                     break
               else: 
                     print("Error, unknown option {}.".format(choice))
         
         elif choice == '6':
               
               register(garth)
               print("\t1. Return.")
               choice = input(">> ")
               print()

               if choice == '1':
                     break
               else: 
                     print("Error, unknown option {}.".format(choice))
         
         elif choice == '7':
               
               register(gert)
               print("\t1. Return.")
               choice = input(">> ")
               print()

               if choice == '1':
                     break
               else: 
                     print("Error, unknown option {}.".format(choice))
         
         elif choice == '8':

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
                     vote(grimp)

                     if choice == '1':
                        break
                     else: 
                        print("Error, unknown option {}.".format(choice))

               elif choice == '2':
               
                     print("\nHello, Gumpy.")
                     vote(gumpy)

                     if choice == '1':
                        break
                     else: 
                        print("Error, unknown option {}.".format(choice))

               elif choice == '3':
               
                     print("\nHello, Grimble.")
                     vote(grimble)

                     if choice == '1':
                        break
                     else: 
                        print("Error, unknown option {}.".format(choice))

               elif choice == '4':
               
                     print("\nHello, Gronk.")
                     vote(gronk)

                     if choice == '1':
                        break
                     else: 
                        print("Error, unknown option {}.".format(choice))
         
               elif choice == '5':
            
                     print("\nHello, Grilbo.")
                     vote(grilbo)

                     if choice == '1':
                        break
                     else: 
                        print("Error, unknown option {}.".format(choice))
         
               elif choice == '6':
               
                     print("\nHello, Garth.")
                     vote(garth)

                     if choice == '1':
                         break
                     else: 
                        print("Error, unknown option {}.".format(choice))
         
               elif choice == '7':
               
                     print("\nHello, Gert.")
                     vote(gert)

                     if choice == '1':
                        break
                     else: 
                        print("Error, unknown option {}.".format(choice))

               elif choice == '8':
               
                     finishVoting()
                     print("\nTallying up the Goblins results.")
                     result = tallyVotes()
                     print("\nThe winner of the Election is")
                     print("\n*Cue drumroll*")
                     print(result)

                     print("Thank you for voting in the Goblin Election.")
                  

               elif choice == '9':
                  print("Returning to Registration\n")
                  break
               
               else: 
                     print("Error, unknown option {}.".format(choice))

         elif choice == '9':
            print("Goodbye, Goblin! \n")
            break
         
         else: 
            print("Error, unknown option {}.".format(choice))