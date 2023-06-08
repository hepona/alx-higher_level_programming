#!/usr/bin/python3
import sys
if __name__ == "__main__":
    l = len(sys.argv)
    if l == 1:
        print("{} arguments.".format(l - 1))
    elif l == 2:
        print("{} argument: ".format(l - 1))
        print("{}: {}".format(l - 1, sys.argv[l - 1]))
    else:
        print("{} arguments: ".format(l - 1))
        for i in range(1, l):
            print("{}: {}".format(i, sys.argv[i]))
