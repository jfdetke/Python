#!/usr/bin/env python3

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

for i in range(1,17):
    groupbuzz(i)
