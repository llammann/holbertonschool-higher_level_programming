#!/usr/bin/python3
alphabet = ''
for alpha in range(97, 123):
    if (chr(alpha) == 'q' or chr(alpha) == 'e'):
        continue
    else:
        alphabet += chr(alpha)
print("{}".format(alphabet), end="")
