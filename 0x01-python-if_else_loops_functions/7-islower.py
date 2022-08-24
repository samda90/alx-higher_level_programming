#!/usr/bin/python3
def islower(c):
    for i in range(97, 122):
        if c == chr(i):
            return True
        else:
            return False
