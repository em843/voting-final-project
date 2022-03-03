MrGrumbleCount = 0
MadamGoobCount = 0

if __name__ == "__main__":
    
    

    while True: 
        print("\nWelcome to the Goblin Voting System")
        print("--------------------------------------- ")
        print("\t1. User1")
        print("\t2. User2")
        print("\t3. User3")   
        print("\t6. Quit \n")
        choice = input(">> ")
        print()

        if choice == '1':
            
            print("\nHello, Grimp. What would you like to do?")
            print("------------------------------------------- ")
            print("\t1. Register to vote")
            print("\t2. Cast vote")
            print("\t6. Quit \n")
            choice = input(">> ")
            print()
            

            if choice == '1':
                print("Here is your validation number and CTR key sent as encrypted text.") #publiic key
                print("Here it is decrypted with your private key.")
            
            elif choice == '2':
                message = input("\nPlease input your validation number: ") #if it exists in our data and matches the name Grinkle, cont.
                #check if they have voted before. if so then accuse them of treason and break. 
                print("Please input your vote. Type 1 for Mr. Goblin, or 2 for Gert.")
                choice = input("Vote: ") 
                if choice == '1':
                    MrGrumbleCount += 1 
                elif choice == '2':
                    MadamGoobCount += 1
                else:
                     print("Error, unknown option {}.".format(choice))

                print("Your signature is...") #generating the signature required the message, so we should do this for them.
                print("Please input/here is your CTR key") #will be easier to just have the program do it for the goblins
                print("Here is your encrypted message. It will be sent for you, thank you for voting!")
                #We crete and send the encrypted message for them. 
                #When it 'gets to the CTA', when the signature is verified, then we will record that they already voted so they cant again. 
                #we will also need to add their validation number to a list with eveyrone else who voted for that canidate.

            elif choice == '6':
                print("Goodbye, Goblin! \n")
                break

            else: 
                print("Error, unknown option {}.".format(choice))



        elif choice == '2': #user2
            print("\nHello, Gumpy. What would you like to do?")



        elif choice == '3': #user3
            print("\nHello, Grank. What would you like to do?")



        


        elif choice == '6':
            print("Goodbye, Goblin! \n")
            break

        else:
            print("unknown option {}.".format(choice))
