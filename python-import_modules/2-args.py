#!/usr/bin/python3
import sys


def main():
    argv = sys.argv[1:]
    arg_count = len(argv)

    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print(f"{arg_count} arguments:")

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
