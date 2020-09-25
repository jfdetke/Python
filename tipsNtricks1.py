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


## https://medium.com/analytics-vidhya/interesting-python-tips-and-tricks-6d033967b5a5
def unpack_tuple():
    print("Unpacking tuple")
    t = (0,1,2)
    a,b,c= t
    print(f"a is {a}")

    #   Nested
    print("Nesting tuple")
    t =(0,2,(2,3,4))
    a,b,c=t
    print(f"a is {a}")
    print(f"b is {b}")
    print(f"c is {c}")
    print("---------")

    #
    t = (0,1,2,3,4)
    a,b,*c = t
    print(f"a is {a}")
    print(f"b is {b}")
    print(f"c is {c}")
    print("---------")
    a,*b,c = t
    print(f"a is {a}")
    print(f"b is {b}")
    print(f"c is {c}")
    print("---------")
    #   convention: "_" used for thowaway parts
    a,*_,c = t
    print(f"a is {a}")
    print(f"c is {c}")
    print("---------")
    t = (0,1,2)
    a,*b,c = t  # *b will create a list
    print(f"a is {a}")
    print(f"b is {b}")
    print(f"c is {c}")
    print("---------")

    a,b,c,*d = t
    print(f"a is {a}")
    print(f"b is {b}")
    print(f"c is {c}")
    print(f"d is {d}")  # since there were no 'extra' elements, this will be an empty list
    if d :
        print(f"d is {d}")
    else:
        print(f"d :{d} should be empty list")
    print("---------")


def unpack_list():
    print("Unpacking list")
    l = [0,1,2]
    a,b,c = l
    print(f"a is {a}")
    print(f"c is {c}")
    #
    print("nested list")
    l = (0,1,(2,3,4))
    a,b,c = l
    print(f"a is {a}")
    print(f"b is {b}")
    print(f"c is {c}")
    for i in l:
        print(i)

def main():
    print("Hello, main")
    ##groupbuzz(3)
    unpack_tuple()
    unpack_list()

if __name__ == "__main__":
    main()
