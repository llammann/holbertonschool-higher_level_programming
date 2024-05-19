#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5

    results = [
        "{} + {} = {}".format(a, b, add(a, b)),
        "{} - {} = {}".format(a, b, sub(a, b)),
        "{} * {} = {}".format(a, b, mul(a, b)),
        "{} / {} = {}".format(a, b, div(a, b))
    ]

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
