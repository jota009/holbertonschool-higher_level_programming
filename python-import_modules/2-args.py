#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = len(argv) - 1

    if count == 0:
        print("0 arguments.")
    else:
        print("{} {}:".format(
            count,
            "argument" if count == 1 else "arguments"
            ))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
