#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ln = len(argv)
    r = 0
    for i in range(1, ln):
        r = r + argv[i]
    print("{}".format(r))
