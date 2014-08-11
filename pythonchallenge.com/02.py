#!/usr/bin/env python3

def decode(text):
    for i in text:
        if 97 <= ord(i) < 121:
            print (chr(ord(i) + 2), end = '')
        elif 121 <= ord(i) <= 122:
            print (chr(ord(i) + 2 - (122 - 96)), end = '')
        else:
            print (i, end ='')
    print()

def main():
    text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. '''

    print (ord('a'), ord('z'))
    print ()
    
    decode(text)
    decode("map")
    
if __name__ == '__main__':
    main()