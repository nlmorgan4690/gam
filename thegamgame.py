

import csv
import os


username = input("Enter full DCSD email address: ")
messageid = input("What is the message ID you are looking for? ")

runthegam = "gam users " + username + " delete messages query rfc822msgid:" + messageid + " doit"

print (runthegam)

os.system(runthegam)