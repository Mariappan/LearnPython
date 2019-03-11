#!/usr/bin/python
import ast

with open('roomsinput_orig.txt') as f:
    content = f.readlines()
content = ast.literal_eval('['+content[0]+']')

for i in content:
    [m, n, u] = i
    print(m,n,u)
