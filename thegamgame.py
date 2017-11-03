

import csv
import os


username = "Enter full DCSD email address OR type quit to close the program:\n "
messageid = "What is the message ID you are looking for?\n "


def gam_script():
    active = True
    runthegam = "gam users " + username + " delete messages query rfc822msgid:" + messageid + " doit"
    while active:
        message_one = raw_input(username)
        if message_one == "quit":
            active = False
            break
        message_two = raw_input(messageid)
        if message_two == "quit":
            active = False
            break
        else:
            print(runthegam)
            os.system(runthegam)


gam_script()