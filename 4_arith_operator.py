#!/usr/bin/env python3

def main():
    print ('Arithmetic Operators\n')
    a , b = 10 , 3
    
    print("a and b is ", a,b)
    
    print("Operator")
    print("+ =", a+b)
    print("- =", a - b )
    print("/ =", a/b)
    print("// =", a//b)
    print("% =", a % b)
    
    print('\n\nround() method for rounding off decimal values')
    print("/ =", a/b)
    print("/ =", round(a/b))
    print("/ =", round(a/b, 2))
    
    a , b = 2 , 3
    
    print("\na and b is ", a, b)
    
    print("Operator")
    print("+ =", a+b)
    print("- =", a - b )
    print("/ =", a/b)
    print("// =", a//b)
    print("% =", a % b)

if __name__ == '__main__':
    main()
