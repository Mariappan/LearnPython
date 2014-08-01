#!/usr/bin/env python3


def main():
    print ("-----------------\n  print() Usage\n-----------------\n")
    print ("In print(), ',' add a space between strings. '+' - just concatanate")
    print ()

    print ('print ("This" , "is" , "a" , "test");')
    print ("This" , "is" , "a" , "test\n")

    print ('print ("This", "is", "a", "test");')
    print ("This", "is", "a", "test\n")

    print ('print ("This" + "is" + "another" + "test");')
    print ("This" + "is" + "another" + "test\n")
    
    # The variable scope is local
    a = 10
    s = "Value of a is {}".format(a)        # format() - to format the string
    print("\ns = \"Value of a is {}\".format(a)")
    print(s)

    print ("~End")

if __name__ == '__main__':
    main()
