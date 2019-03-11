#!/usr/bin/env python

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    print ("Stack: ", stack)
    while stack:
        (vertex, path) = stack.pop()
        print ("Vertex: ", vertex, " path: ", path)
        for next in graph[vertex] - set(path):
            if next == goal:
                print ("Solution: ", path + [next], "\n")
                yield path + [next]
            else:
                stack.append((next, path + [next]))
                print ("Appending Stack: ", stack)

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
paths = list(dfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

print("Paths are ", paths)
