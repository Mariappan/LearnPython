#!/usr/bin/env python3

def main():
    """Main function"""
    print ("2 < 3 :", 2 < 3)
    print ("2 > 3 :", 2 > 3)
    print ()
    
    print ("type(True):{} type(False){}".format(type(True), type(False)))
    
    print ("\nString also can be compared")
    print ("'cat' < 'dog'", 'cat' < 'dog')
    print ()
    
    # Syntactic sugar
    x = 10
    print ("2 < x < 5 :", 2 < x < 5)
    print ("12 < x < 15 :", 12 < x < 15)
    print ("2 < x < 15 :", 2 < x < 15)
    
    print ("\nBoolean Operators: and or not")
    
    print ("\nAnd")
    print ("True and True :", True and True)
    print ("True and False :", True and False)
    print ("False and True :", False and True)
    print ("False and False :", False and False)
    
    print ("\nOr")
    print ("True or True :", True or True)
    print ("True or False :", True or False)
    print ("False or True :", False or True)
    print ("False or False :", False or False)
    
    print ("\nNot")
    print ("not True :", not True)
    print ("not False :", not False)

if __name__ == '__main__':
    main()