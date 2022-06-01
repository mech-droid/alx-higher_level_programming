#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print("{}".format((str) - 35), end="")
        else:
            print("{}".format(str), end="")
