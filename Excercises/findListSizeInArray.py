#!/usr/bin/env python

def solution(A):
    # write your code in Python 3.6
    index=0
    count=0
    viewedIndex = set()

    while (index not in viewedIndex) and index !=-1:
        viewedIndex.add(index)
        index=A[index]
        count+=1

    return count

a = [1, 4, -1, 3, 2]
print ("Count is " + str(solution(a)))
