#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    all = dir(hidden_4)
    for one in all:
        if one[:2] != "__":
            print(one)
