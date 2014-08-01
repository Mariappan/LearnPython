#!/usr/bin/env python3


def main():
    print ("-----------------\n  print() Usage\n-----------------")
    print ("In print(), ',' add a space between strings. '+' - just concatanate")
    print ()

    print ('print ("This" , "is" , "a" , "test");')
    print ("This" , "is" , "a" , "test\n")

    print ('print ("This", "is", "a", "test");')
    print ("This", "is", "a", "test\n")

    print ('print ("This" + "is" + "another" + "test");')
    print ("This" + "is" + "another" + "test\n")

    print ("~End")

if __name__ == '__main__':
    main()
