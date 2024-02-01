#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Iterate through each integer in the data set
    for byte in data:
        # Check if the current byte is a continuation byte
        if num_bytes == 0:
            if (byte >> 7) == 0b0:
                continue
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            # Check if the current byte is a valid continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1
    
    # Check if there are any incomplete UTF-8 characters
    return num_bytes == 0


