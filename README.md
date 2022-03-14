# voting-final-project
Virtual Election Booth: 
This project implements the secure election protocol 
for voting with two central facilities. These two facilities are CLA and CTF.
Our goal is to make the voting process as secure as possible to maintain individual
privacy and prevent cheating. Thus, we have implemented signatures and AES keys to
encrypt and decrypt for the user.

Description: 
The CLA Certifies the voters. The voter will first send a message to CLA asking for a
validation number and CLA will return a random validation number. CLA has a list of validation 
numbers and a list of validation number recipients to prevent voters from voting twice. Then 
CLA will send the list of validation numbers to CTF.

The CTF basically counts the votes. If the validation number is there, CTF will take the 
validation number out of the list to prevent voting twice. Then it adds the validation number to 
the list of people who voted for a particular candidate and adds one to the tally. Once all 
votes have been received, CTF publishes the outcome.
 
Our program combines the two facilities into one file named functions.py. We stored all of
the keys and validation numbers in data.py. All messages passed between the 
various parties are encrypted and signed, preventing impersonating or intercepting 
transmissions. Our encryption is done using AES and signing is done by RSA.

How to Use our Project:
Our user interface is in the file named main_menu.py. Run the file to register and vote
for each individual user which we can call option (1.) OR register and vote for all users 
which we can call option (2.). For (1.), you can register for any of the users from choices 
1-7. Choice 9 will exit the user out of the program. The register section is mainly to check 
if the register function works correctly. This function will check the identity of the user to
avoid impersonation and it will also check if the user has already registered to avoid voting 
twice. Once you are done with (1.), you may move on to choice 8. In the next section, it will 
automatically register all users that have NOT yet registered. You can then vote for any of the
users from 1-7. Choice 9 will bring you back to the register menu. The voting section will allow
the user to vote for a candidate and verify their vote. Verifying their vote will check if their 
validation number matches the list from CLA and will check if the user has already voted. Once 
you have finished voting, choose option 8 to run the election. In this section, it will 
automatically vote for any user who has NOT voted yet. It will then tally up the votes and 
return the candidate that has the most votes. It will also tell the user how many votes the 
candidate has in the end. 

For option (2.), the user can test the program quickly. In the register menu, choose choice 8. 
Choice 8 will register all the users and move onto the voting section. In the voting section,
choose choice 8 to run election. This will automatically vote for all the users and then return
the candidate with the most votes. Again, choices 9 on both menus will exit the user out of
each screen.

Credits: Tabitha Rowland, Robin Vogel, Erin Murphy, and Vien Hang.