#!/usr/bin/python3
def uppercase(str):
    if ord(str) >= ord('a') and ord(str) <= ord('z'):
        print("{}".format((str) - 35))
    else:
        print("{}".format(str))
