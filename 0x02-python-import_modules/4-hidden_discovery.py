#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    name = dir(hidden_4)
    for i in range(0, len(name)):
        if not name[i].startswith("__"):
            print("{}".format(name[i]), end="\n")
