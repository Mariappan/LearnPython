#!/usr/bin/env python
"""
Created on Mon Mar  4 16:43:25 2019

@author: Mariappan
"""

import re

def fill_alternates(matrix,startswith):
    filled = 0
    n_start = 0 if startswith == 1 else 1
    #for even rows and columns
    for i in range(0,m,2):
        for j in range(n_start,n,2):
            matrix[i][j]=1
            filled+=1
    #for odd rows and columns
    n_start = 1 if startswith == 1 else 0
    for i in range(1,m,2):
        for j in range(n_start,n,2):
            matrix[i][j]=1
            filled+=1

    return (filled,matrix)

def fill_remaining(matrix,startswith,filled):
    rows=[0,m-1] # First and last row
    columns=[0,n-1] # First and last column

    # First fill Corner elements 
    for i in rows:
        for j in columns:
            if filled==u: return (filled,matrix)
            if matrix[i][j]==0:
                matrix[i][j]=1
                filled+=1

    # To fill first and last rows
    for i in rows:
        for j in range(n):
            if filled==u: return (filled,matrix)
            if matrix[i][j]==0:
                matrix[i][j]=1
                filled+=1

    # To fill first and last columns
    for j in columns:
        for i in range(m):
            if filled==u: return (filled,matrix)
            if matrix[i][j]==0:
                matrix[i][j]=1
                filled+=1

    # Fill remaining rooms (Reverse logic of fill_alternates)
    # for even rows and columns
    n_start = 1 if startswith == 1 else 0
    for i in range(0,m,2):
        for j in range(n_start,n,2):
            if filled==u: return (filled,matrix)
            if matrix[i][j] == 0:
                matrix[i][j]=1
                filled+=1

    #for odd rows and columns
    n_start = 0 if startswith == 1 else 1
    for i in range(1,m,2):
        for j in range(n_start,n,2):
            if filled==u: return (filled,matrix)
            if matrix[i][j] == 0:
                matrix[i][j]=1
                filled+=1

    return (filled,matrix)

def countNeighbours(matrix,m,n):
    count=0
    x=[0,0,1,-1]
    y=[1,-1,0,0]
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==1:
                for k in range(4):
                    newx=i+x[k]
                    newy=j+y[k]
                    if newx>=0 and newx<m and newy>=0 and newy<n and matrix[newx][newy]==1:
                        count+=1
            matrix[i][j]=0
    return count


def find_best(m,n,u):
    if u > (m*n):
        return 0

    # The users can be filled in alternate rooms
    if u <= (m*n)//2:
        return 0

    matrix=[0]*m
    for i in range(m):
        matrix[i] = [0]*n

    startswith = 0
    filled,matrix = fill_alternates(matrix,startswith)
    #print("Fill_Alternatives:\n",matrix)
    if filled != u:
        filled,matrix = fill_remaining(matrix,startswith,filled)
    #print("Fill_Remaining:\n",matrix)
    neighbours0=countNeighbours(matrix,m,n)
    #print("StartswithZero",neighbours0)

    startswith = 1
    filled,matrix = fill_alternates(matrix,startswith)
    #print("Fill_Alternatives:\n",matrix)
    filled,matrix = fill_remaining(matrix,startswith,filled)
    #print("Fill_Remaining:\n",matrix)
    neighbours1=countNeighbours(matrix,m,n)
    #print("StartswithOne",neighbours1)

    return min(neighbours0, neighbours1)

"""
inp_list=input().split()
m=int(inp_list[0])
n=int(inp_list[1])
u=int(inp_list[2])
program_output=find_best(m,n,u)
print("\n\n OUTPUT:\n")
print("[",m,",",n,",",u,"]->",program_output)

"""
s="""[5,2,8]-> 7
[4,3,12]-> 17
[16,1,9]-> 1
[5,2,6]-> 2
[2,4,6]-> 4
[3,5,14]-> 18
[5,3,13]-> 14
[3,5,15]-> 22
[3,4,12]-> 17
[1,16,7]-> 0
[1,16,1]-> 0
[2,4,5]-> 2
[1,15,1]-> 0
[2,3,6]-> 7
[3,5,12]-> 11
[3,5,1]-> 0
[5,3,5]-> 0
[1,15,0]-> 0
[1,1,1]-> 0
[1,16,8]-> 0
[8,2,12]-> 10
[16,1,16]-> 15
[2,5,9]-> 10
[15,1,1]-> 0
[4,4,1]-> 0
[16,1,1]-> 0
[2,5,8]-> 7
[3,5,10]-> 6
[1,16,16]-> 15
[3,5,0]-> 0
[3,3,6]-> 3
[5,3,4]-> 0
[1,15,15]-> 14
[2,2,2]-> 0
[3,5,8]-> 0
[2,6,12]-> 16
[5,3,10]-> 6
[3,2,0]-> 0
[3,3,9]-> 12
[1,16,0]-> 0
[15,1,0]-> 0
[4,4,7]-> 0
[5,3,2]-> 0
[16,1,8]-> 0
[5,3,3]-> 0
[5,3,7]-> 0
[3,5,9]-> 3
[5,3,1]-> 0
[9,1,6]-> 2
[5,3,0]-> 0
[4,3,5]-> 0
[4,2,2]-> 0
[5,2,4]-> 0
[5,3,12]-> 11
[1,13,9]-> 4
[3,5,11]-> 8
[4,4,15]-> 20
[3,5,4]-> 0
[2,2,3]-> 2
[3,5,2]-> 0
[7,2,13]-> 16
[2,2,4]-> 4
[2,7,13]-> 16
[3,5,7]-> 0
[1,9,6]-> 2
[15,1,6]-> 0
[5,3,11]-> 8
[3,3,0]-> 0
[7,2,0]-> 0
[6,2,12]-> 16
[15,1,15]-> 14
[4,4,8]-> 0
[7,2,11]-> 10
[4,3,6]-> 0
[4,3,8]-> 4
[4,4,9]-> 2
[1,16,9]-> 1
[4,4,0]-> 0
[2,3,4]-> 2
[3,5,5]-> 0
[5,3,8]-> 0
[4,4,16]-> 24
[1,1,0]-> 0
[1,15,8]-> 0
[5,3,14]-> 18
[3,5,6]-> 0
[1,15,6]-> 0
[2,6,9]-> 7
[16,1,0]-> 0
[4,3,7]-> 2
[16,1,7]-> 0
[15,1,8]-> 0
[3,5,3]-> 0
[5,3,9]-> 3
[6,2,4]-> 0
[1,15,7]-> 0
[5,3,6]-> 0
[5,3,15]-> 22
[15,1,7]-> 0
[5,5,23]-> 32
[3,5,1]-> 0"""

pattern = re.compile(r'\s*\[(\d+),(\d+),(\d+)\]->\s*(\d+)\s*')
for line in s.splitlines():
    match = re.search(pattern,line)
    if match:
        m=int(match.group(1))
        n=int(match.group(2))
        u=int(match.group(3))
        expected_output=int(match.group(4))
        #print(m,n,u,expected_output)
        program_output=find_best(m,n,u)
        #print("\n\n OUTPUT:\n")
        print("[",m,",",n,",",u,"]->",program_output)
        if program_output != expected_output:
            print("WRONG")
            print("[",m,",",n,",",u,"]->",program_output)
            print("EXpected")
            print("[",m,",",n,",",u,"]->",expected_output)

def extract_data2(s):
    global pattern
    match = pattern.match(s)
    m = int(match.group("m"))
    n = int(match.group("n"))
    u = int(match.group("u"))
    exp = int(match.group("e"))

    return (m, n, u, exp)

# pattern = re.compile(r"""\[(?P<m>.*?)\,(?P<n>.*?),(?P<u>.*?),(?P<e>.*?)\]""", re.VERBOSE)
# with open('roomsinput.txt') as f:
#     content = f.readlines()
# content = [x.strip() for x in content]

# for i in content:
#     m, n, u, exp = extract_data2(i)

#     # print(i)
#     # print("[" + str(m) + "," + str(n) + "," + str(u) + "]->" + str(find_best(m,n,u)))
#     # print("\n")
#     output_score = find_best(m,n,u)
#     if output_score != exp:
#         print(i)
#         print("[" + str(m) + "," + str(n) + "," + str(u) + "]->" + str(output_score))
#         print("\n")
