#!/usr/bin/python3
"""
Defines a function that determines whether a list of
integers passed into it conforms
to UTF-8 format.
"""
def validUTF8(data):
    """
    Takes a list of ints and returns true if the list is
    a valid UTF-8 encoding, else returns false
    Args:
        data : List of ints representing possible UTF-8 encoding
    Return:
        bool : True or False
    """
    num_bytes = 0
    
    for num in data:
        if num_bytes == 0:
            if (num >> 7) == 0b0:
                continue
            elif (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1
    
    return num_bytes == 0

