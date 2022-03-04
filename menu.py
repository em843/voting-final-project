"""
Authors: Tabitha Rowland, Robin Vogel, Erin Murphy, Vien Hang


Main menu where the user will choose what they want to do.


"""

MrGrumbleCount = 0
MadamGoobCount = 0

if __name__ == "__main__":
    
    

    while True: 
        print("\nWelcome to the Goblin Voting System")
        print("--------------------------------------- ")
        print("\t1. Grimp")
        print("\t2. Gumpy")
        print("\t3. Grimble")   
        print("\t4. Gronk")
        print("\t5. Grilbo")
        print("\t6. Garth")
        print("\t7. Gert")
        print("\t8. Gyre")
        print("\t9. Quit \n")
        choice = input(">> ")
        print()

        if choice == '1':
            
            print("\nHello, Grimp. What would you like to do?")
            print("------------------------------------------- ")
            print("\t1. Register to vote")
            print("\t2. Cast vote")
            print("\t3. Verify vote")
            print("\t4. Request results")
            print("\t5. Quit \n")
            choice = input(">> ")
            print()
            
            # Register to vote
            if choice == '1':
                print("Here is your validation number and CTR key sent as encrypted text:") #public key
                print("Here it is decrypted with your private key:")
                print("Your signature is...") #generating the signature required the message, so we should do this for them.
                print("Please input/here is your CTR key") #will be easier to just have the program do it for the goblins
                print("Here is your encrypted message. It will be sent for you, thank you for voting!")
                #We crete and send the encrypted message for them. 
                #When it 'gets to the CTA', when the signature is verified, then we will record that they already voted so they cant again. 
                #we will also need to add their validation number to a list with eveyrone else who voted for that canidate.
            
            # Cast vote
            elif choice == '2':
                message = input("\nPlease input your validation number: ") #if it exists in our data and matches the name Gimp, cont.
                #check if they have voted before. if so then accuse them of treason and break. 
                print("Please input your vote. Type 1 for Mr. Grumble, or 2 for Madam Goob.")
                choice = input("Vote: ") 
                if choice == '1':
                    MrGrumbleCount += 1 
                    break
                elif choice == '2':
                    MadamGoobCount += 1
                    break
                else:
                     print("Error, unknown option {}.".format(choice))

                print("Your signature is...") #generating the signature required the message, so we should do this for them.
                print("Please input/here is your CTR key") #will be easier to just have the program do it for the goblins
                print("Here is your encrypted message. It will be sent for you, thank you for voting!")
                #We crete and send the encrypted message for them. 
                #When it 'gets to the CTA', when the signature is verified, then we will record that they already voted so they cant again. 
                #we will also need to add their validation number to a list with eveyrone else who voted for that canidate.
                
            #Verify vote    
            elif choice == '3':
                # need validation id from user. Then CTF decrypts the key using RSA private key
                validation = input("Please enter your validation number: ")
                # if validation == True:
                    # return verification status and voter name
                # else:
                    # print("Incorrect validation number.")
                    
                break
            
            #Request results
            elif choice == '4':
                validation = input("Please enter your validation number: ")
                # if validation == true:
                    #return results
                # else:
                    # print("Incorrect validation number.")
                break
            
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
            print("\nHello, Gyre. What would you like to do?")
            break

        elif choice == '9':
            print("Goodbye, Goblin! \n")
            break

        else:
            print("unknown option {}.".format(choice))
