#!/usr/bin/env python
def main():
    """ Main Module """
    print ("""\
    =======================
      Datatypes in Python
    =======================""")
    
    print('Integer Datatypes')
    a, b = 1, 2
    print("a, b = 1, 2")
    print("a is ", a, 'and b is', b)
    
    print('\nFloat Datatypes')
    a, b = float(1), float(2)
    print("a, b = float(1), float(2)")
    print("a is ", a, 'and b is', b)
    
    a, b = int(1.1), float(2)
    print("\na, b = int(1.1), float(2)")
    print("a is ", a, 'and b is', b)
    
    print('\nString Datatypes')
    s = "This is an example"
    print("s = \"This is an example\"")
    print("s is ", s)
    
    s = "Value of a is {}".format(a)
    print("\ns = \"Value of a is {}\".format(a)")
    print(s)
    
    print('\nTuple Datatypes (Immutable)')
    x = (1, 2, 3)
    print("x = (1, 2, 3)")
    print(x)
    
    y , z = (1, 2, 3), (4, 5, 6)
    print ("\ny , z = (1, 2, 3), (4, 5, 6)")
    print("y ", y, "z ", z)
    
    print("\nId of x and y is ", id(x), id(y))
    
    print('\nList Datatypes (Mutable)')
    x = [1, 2, 3]
    print("x = [1, 2, 3]")
    print(x)
    
    y , z = [1, 2, 3], [4, 5, 6]
    print ("\ny , z = [1, 2, 3], [4, 5, 6]")
    print("y ", y, "z ", z)
    
    print("Id of x and y is ", id(x), id(y))

if __name__ == '__main__':
    main()