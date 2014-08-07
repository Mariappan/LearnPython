#!/usr/bin/env python3

def reverse(orig_string):
    print ("Method \n------")
    print (orig_string, reversed(orig_string))
    message = "".join(reversed(orig_string))
    print (message, type(message))
    
    print ("".join(reversed(orig_string)))
    
def reverse2(orig_string):
    print ("\n\nMethod 2 \n--------")
    orig_list = list(orig_string)
    orig_list.reverse()
    print (orig_list)
    message = "".join(orig_list)
    print (message, type(message))
    
    
def reverse3(orig_string):
    print ("\n\nMethod 3 \n--------")
    orig_list = list(orig_string)
    
    rev_list = []
    for i in range(len(orig_list)):
        rev_list.insert(0, orig_list[i])
        print (rev_list)

    message = ''
    for character in rev_list:
        message += character
        print (message)
    
    print (message, type(message))    
    
def conf_reverse(text):
    if len(text) <= 1:
        return text
    print (text[1:], '+', text[0])
    return conf_reverse(text[1:]) + text[0]

def main():
    reverse("Testing")
    reverse2("Testing")
    reverse3("Testing")
    print ("\n\nRecursion Method 3 \n----------------")
    print (conf_reverse("Testing"))
    

if __name__ == '__main__':
    main()