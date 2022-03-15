"""
Authors: Tabitha Rowland, Robin Vogel, Erin Murphy, Vien Hang



Each person has their own public and private key
We create a secret to send them, encrypt it with the public key, and they can decrypt it with their private key


"""
from unittest import result
from data import *
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
         print("\t8. Vote.")
         print("\t9. Quit.")
         choice = input(">> ")
         print()

         if choice == '1':
               register(grimp, False)
               print("\t1. Return.")
               choice = input(">> ")
               print()

               if choice == '1':
                     continue
               else: 
                     print("Error, unknown option {}.".format(choice))
         
         elif choice == '2':
               
               register(gumpy, False)
               print("\t1. Return.")
               choice = input(">> ")
               print()

               if choice == '1':
                     continue
               else: 
                     print("Error, unknown option {}.".format(choice))
         
         elif choice == '3':
               
               register(grimble, False)
               print("\t1. Return.")
               choice = input(">> ")
               print()

               if choice == '1':
                     continue
               else: 
                     print("Error, unknown option {}.".format(choice))
         
         elif choice == '4':
               
               register(gronk, False)
               print("\t1. Return.")
               choice = input(">> ")
               print()

               if choice == '1':
                     continue
               else: 
                     print("Error, unknown option {}.".format(choice))
         
         elif choice == '5':
               
               register(grilbo, False)
               print("\t1. Return.")
               choice = input(">> ")
               print()

               if choice == '1':
                     continue
               else: 
                     print("Error, unknown option {}.".format(choice))
         
         elif choice == '6':
               
               register(garth, False)
               print("\t1. Return.")
               choice = input(">> ")
               print()

               if choice == '1':
                     continue
               else: 
                     print("Error, unknown option {}.".format(choice))
         
         elif choice == '7':
               
               register(gert, False)
               print("\t1. Return.")
               choice = input(">> ")
               print()

               if choice == '1':
                     continue
               else: 
                     print("Error, unknown option {}.".format(choice))
         
         elif choice == '8':
            while True:
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
                     verify_vote(grimp, vote(grimp))
                     print("\t1. Return.")
                     choice = input(">> ")
                     print()

                     if choice == '1':
                        continue
                     else: 
                        print("Error, unknown option {}.".format(choice))

               elif choice == '2':
               
                     print("\nHello, Gumpy.")
                     verify_vote(gumpy, vote(gumpy))
                     print("\t1. Return.")
                     choice = input(">> ")
                     print()

                     if choice == '1':
                        continue
                     else: 
                        print("Error, unknown option {}.".format(choice))

               elif choice == '3':
               
                     print("\nHello, Grimble.")
                     verify_vote(grimble, vote(grimble))
                     print("\t1. Return.")
                     choice = input(">> ")
                     print()

                     if choice == '1':
                        continue
                     else: 
                        print("Error, unknown option {}.".format(choice))

               elif choice == '4':
               
                     print("\nHello, Gronk.")
                     verify_vote(gronk, vote(gronk))
                     print("\t1. Return.")
                     choice = input(">> ")
                     print()

                     if choice == '1':
                        continue
                     else: 
                        print("Error, unknown option {}.".format(choice))
         
               elif choice == '5':
            
                     print("\nHello, Grilbo.")
                     verify_vote(grilbo, vote(grilbo))
                     print("\t1. Return.")
                     choice = input(">> ")
                     print()

                     if choice == '1':
                        continue
                     else: 
                        print("Error, unknown option {}.".format(choice))
         
               elif choice == '6':
               
                     print("\nHello, Garth.")
                     verify_vote(garth, vote(garth))
                     print("\t1. Return.")
                     choice = input(">> ")
                     print()

                     if choice == '1':
                         continue
                     else: 
                        print("Error, unknown option {}.".format(choice))
         
               elif choice == '7':
               
                     print("\nHello, Gert.")
                     verify_vote(gert, vote(gert))
                     print("\t1. Return.")
                     choice = input(">> ")
                     print()

                     if choice == '1':
                        continue
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
                     print("To run another election please restart the program.\n")
                     break
                  

               elif choice == '9':
                  print("Returning to registering screen\n")
                  print("In order to fully leave choose quit again\n")
                  break
               
               else: 
                     print("Error, unknown option {}.".format(choice))

         elif choice == '9':
            print("Goodbye, Goblin! \n")
            break
         
         else: 
            print("Error, unknown option {}.".format(choice))
         break
      