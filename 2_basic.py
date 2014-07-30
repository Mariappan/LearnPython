#!/usr/bin/env python3

# In python everything is object
# a = 1 is also a object.

# type(a), id(a)

def main():
    work()
    end()

def work():
    
    # To print Empty lines
    print()
    
    print("Lets assign values to a, b")
    a = 1
    print('a=1')
    
    # , in print add spaces in output
    print("a is ", type(a), id(a), a)
    print("a is ",type(a),id(a),a) # See the output of above two values

    b = 1
    print('\nb=1')
    print("b is ", type(b), id(b), b)
    print ("Id of a and b are same\n")

    m = a
    print('m=a')
    # In print, ',' should be written between two objects.
    print("m is ", type(m), id(m), m, "It works")

    # To find, whether the values are equal
    print("a==b:", a==b)
   
    # To find whether it is a same object
    print("a is b: ", a is b)

    a = 2
    print('\nChange a=2')
    print(type(a), id(a), a)
    print("a==b:", a==m)
    print("a is b: ", a is m)


def end():
    print ("\nEnd of Program~")

if __name__ == '__main__':
    main()
