"""
Authors: Tabitha Rowland, Robin Vogel, Erin Murphy, Vien Hang


Main menu where the user will choose what they want to do.


"""

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
            print("\t3. Verify vote.")
            print("\t4. Request results.")
            print("\t5. Quit \n")
            choice = input(">> ")
            print()
            
            # Register to vote
            if choice == '1':
                print("Here is your signature number:")
                print("Your signature number has been verified!")
                print("Here is your encrypted AES key:")
                print("Here is your decrypted AES key:")
                print("Your validation number has been generated, thank you for registering!")
                
            # Cast vote
            elif choice == '2':
                print("Here is your signature number:")
                print("Your signature number has been verified!")
                print("Here is your encrypted AES message:")
                print("Here is your decrypted AES message:")
                # Vote
                print("Please input your vote. Type 1 for Mr. Grumble or 2 for Madam Goob.")
                choice = input("Vote: ") 
                print("Your vote has been casted, thank you for voting!")
                
            # Verify vote    
            elif choice == '3':
                print("Here is your validation number:")
                print("Here is your signature number:")
                print("Here is your encrypted AES message:")
                print("Here is your vote:")
            
            # Request results
            elif choice == '4':
                print("Here is the overall voting results:")
                
            # Quit
            elif choice == '5':
                print("Goodbye, Goblin! \n")
                break

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
