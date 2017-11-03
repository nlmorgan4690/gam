

import csv
import os

#create variables that we will call later with a raw_input function
username = "Enter full DCSD email address: \n"
username += 'Type "quit" at anytime to end the program\n'
messageid = "What is the message ID you are looking for?\n "


def gam_script():
    """
    - Creating a function that asks for user input to enter an email address and message id.
    - This input is then placed into gam code and ran on the local machine.
    - When successful, the gam script searches for the email address and deletes the message identified in the
      messageid variable.
    - The script runs continuously until the user types quit.
    """
    active = True
    runthegam = "gam users " + username + " delete messages query rfc822msgid:" + messageid + " doit"
    while active:
        message_one = raw_input(username)
        if message_one == "quit":
            break
        message_two = raw_input(messageid)
        if message_two == "quit":
            break
        else:
            print(runthegam + '\n')
            os.system(runthegam)


gam_script()