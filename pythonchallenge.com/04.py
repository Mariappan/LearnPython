#!/usr/bin/env python3
import re

def isSmall(character):
    if ord('a') <= ord(character) <= ord('z'):
        return True
    else:
        return False

def isCapital(character):
    if ord('A') <= ord(character) <= ord('Z'):
        return True
    else:
        return False

def main():
    """Main Program"""
    
    file = open('equality', 'r')
    buf = file.read()

    for i in range(len(buf) - 7):
        if i == 0:
            continue

        if isSmall(buf[i-1]) and isCapital(buf[i]) and isCapital(buf[i+1]) and isCapital(buf[i+2]) and isSmall(buf[i+3]) \
            and isCapital(buf[i+4]) and isCapital(buf[i+5]) and isCapital(buf[i+6]) and isSmall(buf[i+7]):
            # print (buf[i:i+7])
            print (buf[i+3], end = '')
    file.close()

    # Another Easy way
    print
    print ("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", buf)))

    
if __name__ == '__main__':
    main()
