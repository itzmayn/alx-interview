#!/usr/bin/python3
"""UTF-8 Validation
"""


def validUTF8(data):
    """Determines if a given data set represents
     a valid UTF-8 encoding or not
    """
    count = 0
    for d in data:
        if count == 0:
            if d & 0b10000000 == 0:
                count = 0
            elif d & 0b11100000 == 0b11000000:
                count = 1
            elif d & 0b11110000 == 0b11100000:
                count = 2
            elif d & 0b11111000 == 0b11110000:
                count = 3
            else:
                return False
        else:
            if d & 0b11000000 != 0b10000000:
                return False
            count -= 1
    if count == 0:
        return True
    return False

