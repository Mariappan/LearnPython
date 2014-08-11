#!/usr/bin/env python3


def anagram(strlist):
        import itertools
        return ["".join(perm) for perm in itertools.permutations(strlist)]

def main():
    """Main Program"""
    di = dict()
    
    file = open('ocr', 'r')
    
    for line in file:
        for i in line:
            #print (i, end = '')
            if i in di:
                di[i] = di[i] + 1
            else:
                di[i] = 1
    del i
    file.close()

    #for i in di:
        #print (i, di[i])
        
    strlist = []
    for i in di:
        if di[i] < 100:
            print (i, end = '')
            strlist.append(i)

    del di
    del i
    
    print ("".join(strlist))
    print (anagram(strlist))
    
if __name__ == '__main__':
    main()