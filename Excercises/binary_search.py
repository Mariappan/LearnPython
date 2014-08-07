#!/usr/bin/env python3

def bin_search(li, item, start, end):
    print ('li {} item {} start {} end {} mid {}'. format(li, item, start, end, (start + end)//2))
    
    if end < start:
        return -1
    
    mid = (start + end)//2
    if item < li[mid]:
        return bin_search(li, item, start, mid - 1)
    elif item > li[mid]:
        return bin_search(li, item, mid + 1, end)
    else:
        return mid

def binary_search(li, item):
    return bin_search(li, item, 0, len(li) - 1)


def main():
    li = [2,5,7,9,11,17,22]
    print ('Index of 2 is {}\n'.format(binary_search(li,2)))
    print ('Index of 5 is {}\n'.format(binary_search(li,5)))
    print ('Index of 7 is {}\n'.format(binary_search(li,7)))
    print ('Index of 9 is {}\n'.format(binary_search(li,9)))
    print ('Index of 11 is {}\n'.format(binary_search(li,11)))
    print ('Index of 17 is {}\n'.format(binary_search(li,17)))
    print ('Index of 22 is {}\n'.format(binary_search(li,22)))
    print ('Index of -2 is {}\n'.format(binary_search(li,-2)))
    print ('Index of 23 is {}\n'.format(binary_search(li,23)))
    
    
if __name__ == '__main__':
    main()