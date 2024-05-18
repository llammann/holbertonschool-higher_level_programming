#!/usr/bin/python3

def uppercase(str):
    for let in str:
        if (ord(let) >= ord('a') and ord(let) <= ord('z')):
            let = chr(ord(let) - 32)
        print("{}".format(let), end="")
    print("")
