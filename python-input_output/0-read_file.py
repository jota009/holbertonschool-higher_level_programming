#!/usr/bin/python3
def read_file(filename=""):
    """
    Read a UTF-8 text file and prints its contents to stdout.
    You must use a with-statement here.
    """


    with open(filename, mode="r", encoding="utf-8") as f:
        contents = f.read()
        print(contents, end="")
