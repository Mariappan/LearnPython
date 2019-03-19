#!/usr/bin/env python3
import numpy as np

def findnumpath(a):
    y=len(a)
    x=len(a[0])
    dp=[[0]*x for i in range(y)]
    dp[0][0] = 1
    for yi in range(y):
        for xi in range(x):
            if a[yi][xi]==0:
                continue
            if xi-1>=0:
                dp[yi][xi]+=dp[yi][xi-1]
            if yi-1>=0:
                dp[yi][xi]+=dp[yi-1][xi]
            print(np.array(dp))
    numofpaths=dp[y-1][x-1]%1000000007
    return numofpaths

a = ["11111111", "11111111", "11111111"]
for i in range(len(a)):
    a[i] = [ int(ch) for ch in a[i] ]

print(findnumpath(a))
