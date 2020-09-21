#!/usr/local/bin/python

import datetime
print (datetime.datetime.now())

def groupbuzz(num):
    if (num % 3 == 0 and num % 5 == 0):
        print("GroupON")
    elif (num % 3 == 0 ):
        print("Group")
    elif(num % 5  == 0 ):
        print("On")
    else:
        print(num)

for i in xrange(1,16):
    groupbuzz(i)
