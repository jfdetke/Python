#!/usr/bin/env python3
filename="/etc/csh.logout"
print(filename)

with open(filename,'r') as file:
    for word in file.read().split():
        print(word)
