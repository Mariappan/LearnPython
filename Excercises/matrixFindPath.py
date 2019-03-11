#!/usr/bin/python

import numpy as np
from collections import deque

class Input():
    def __init__(self, strArr):
        index = 0
        for i in strArr:
            strArr[index] = [int(ch) for ch in strArr[index]]
            index += 1
        self.s = strArr
        self.X = len(strArr)
        self.Y = len(strArr[0])

    def is_valid(self, x, y):
        if x >= self.X or y >= self.Y or x < 0 or y < 0:
            return False
        if self.s[x][y] != 0:
            return True
        return False

class Graph():
    def __init__(self, x, y, debug=False):
        self.V = x*y
        self.graph = {}
        for i in range(self.V+1):
            self.graph[i] = set()
        self.debug = debug

    def add_edge(self, src, dst):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dst):
            return
        if self.debug:
            print("Adding edge ", src, dst)
        self.graph[src].add(dst)
        self.graph[dst].add(src)

    def del_edge(self, src, dst):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dst):
            return
        if self.debug:
            print("Deleting edge ", src, dst)
        self.graph[src].discard(dst)
        self.graph[dst].discard(src)

    def is_valid_vertex(self, v):
        return False if v<1 or v>self.V else True

    def print_graph(self):
        print("===================================")
        for key in self.graph:
            print(key, " : ", self.graph[key])
        print("===================================")

    def find_path(self, start, end):
        queue = [(start, [start])]
        while queue:
            (v, path) = queue.pop(0)
            #print(v, path)
            for next in self.graph[v]:
                if next in path:
                    continue
                if next == end:
                    return path + [next]
                queue.append((next, path + [next]))
        return False

def MatrixPath(strArr):
    data = Input(strArr)
    x, y = len(strArr), len(strArr[0])
    g = Graph(x, y)
    v = 1 # vertex
    nodes0 = []
    for i in range(x):
        for j in range(y):
            # data.s[i][j] *= v
            if data.is_valid(i,j):
                if data.is_valid(i, j-1): g.add_edge(v, v-1)
                if data.is_valid(i, j+1): g.add_edge(v, v+1)
                if data.is_valid(i-1, j): g.add_edge(v, v-y)
                if data.is_valid(i+1, j): g.add_edge(v, v+y)
            else:
                nodes0 += [(i, j)]
            v += 1
    print(np.array(data.s))
    # g.print_graph()
    path_present = g.find_path(1, x*y)
    if path_present:
        return True

    numAltPaths = 0
    for i, j in nodes0:
        v = i*y + j + 1
        if data.is_valid(i, j-1): g.add_edge(v, v-1)
        if data.is_valid(i, j+1): g.add_edge(v, v+1)
        if data.is_valid(i-1, j): g.add_edge(v, v-y)
        if data.is_valid(i+1, j): g.add_edge(v, v+y)

        if (g.find_path(1, x*y)):
            # print ("Changing", i, j, "yields a path")
            numAltPaths += 1

        if data.is_valid(i, j-1): g.del_edge(v, v-1)
        if data.is_valid(i, j+1): g.del_edge(v, v+1)
        if data.is_valid(i-1, j): g.del_edge(v, v-y)
        if data.is_valid(i+1, j): g.del_edge(v, v+y)

    return numAltPaths if numAltPaths else "not possible"

inputStr = ["10011101", "11111011", "11010011"]
print (MatrixPath(inputStr))
print ("==============================================")

inputStr = ["10000", "11011", "10101", "11001"]
print (MatrixPath(inputStr))
print ("==============================================")

inputStr = ["1000001", "1001111", "1010101"]
print (MatrixPath(inputStr))
print ("==============================================")

inputStr = ["100", "000", "001"]
print (MatrixPath(inputStr))
print ("==============================================")

inputStr = ["101011", "010011", "111010", "011111"]
print (MatrixPath(inputStr))
print ("==============================================")

inputStr = ["10", "01"]
print (MatrixPath(inputStr))
print ("==============================================")

