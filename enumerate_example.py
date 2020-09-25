#!/usr/bin/env python3
'''
Description goes  here
John F. Detke
jdetke@gmail.com
Version 0.1
'''

def enumerate_examples():
    names = ['Alice', 'Bob', 'Charlie']
    ages  = [24, 50, 18]

    ##for k,v in enumerate(names):
    ##    print(f"k is {k}")
    ##    print(f"v is {v}")

    for i,t in enumerate(zip(names,ages)):
        #   't' will be a tuple
        # print(i,t)
        print(f"{t[0]} is age: {t[1]}")

def main ():
    print("hello main")
    enumerate_examples()

if __name__ == "__main__":
    main()
#######################

# formating print:
# print("{} is new".format(word) )
#
