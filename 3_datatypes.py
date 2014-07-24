#!/usr/bin/env python
def main():
    """ Main Module """
    print ("""\
    =======================
      Datatypes in Python
    =======================""")
    learn_integer()
    learn_float()
    learn_string()
    learn_tuple()
    learn_list()
    learn_asslist()

def learn_integer():
    print('Integer Datatypes')
    print('==================')
    
    # Create and assign two variables in one line
    a, b = 1, 2
    print("a, b = 1, 2")
    print("a is ", a, 'and b is', b)
 
def learn_float():
    print('\nFloat Datatypes')
    print('==================')
    a, b = float(1), float(2)
    print("a, b = float(1), float(2)")
    print("a is ", a, 'and b is', b)
    
    a, b = int(1.1), float(2)
    print("\na, b = int(1.1), float(2)")
    print("a is ", a, 'and b is', b)

def learn_string():
    print('\nString Datatypes')
    print('==================')
    s = "This is an example"
    print("s = \"This is an example\"")
    print("s is ", s)
    
    # The variable scope is local Uncomment the following to run
    a = 10
    s = "Value of a is {}".format(a) # format() - to format the string
    print("\ns = \"Value of a is {}\".format(a)")
    print(s)

def learn_tuple():
    print('\nTuple Datatypes (Immutable)')
    print('==============================')
    x = (1, 2, 3)
    print("x = (1, 2, 3)")
    print(x)
    # Tuple is immutable, i.e Cant change value in tuple
    # But it is faster than list
    #x.append(4)
    print("x.append(4)")
    print(x)
    
    y , z = (1, 2, 3), (4, 5, 6)
    print ("\ny , z = (1, 2, 3), (4, 5, 6)")
    print("y ", y, "z ", z)
    
    print("\nId of x and y is ", id(x), id(y))

def learn_list():
    print('\nList Datatypes (Mutable)')
    print('===========================')
    x = [1, 2, 3]
    print("x = [1, 2, 3]")
    print(x)
    
    x.append(4)
    print ("\nappend() is used to append in the list")
    print("x.append(4)")
    print(x)
    
    x.insert(3, 3.5)
    print ("\ninsert() is used to insert the element in the middle of list")
    print("x.insert(3, 3.5)")
    print(x)
    
    y , z = [1, 2, 3], [4, 5, 6]
    print ("\ny , z = [1, 2, 3], [4, 5, 6]")
    print("y ", y, "z ", z)
    
    print("Id of x and y is ", id(x), id(y))

def learn_asslist():
    """ Assosiative List or Dictionary """
    print('\n\nAssosiative List or Dictionary (Mutable)')
    print('==========================================')
    dic1 = { 'one':1, 'two':2, "three":3 }
    print("dic1 = { 'one':1, 'two':2, \"three\":3 }")
    print(dic1)
    
    # Another Way of declaring a dictionary
    dic2 = dict(
        one = 1,
        two = 2,
        three = 3
    )
    print("\n\n",dic2)
    # Mutable
    dic2['four'] = 'four'
    print(dic2)
    
        
if __name__ == '__main__':
    main()