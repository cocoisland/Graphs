import sys
sys.path.append('..')
from graph.util import Stack
from graph.graph import Graph

# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices :
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Either vertex {v1} or {v2} does not exist.")
            
    def dft(self, starting_node):
        final_path = [starting_node]
        # create an empty set to store visited nodes
        visited = set()
        # create a empty stack and push starting vertex path
        s = Stack() 
        s.push( [starting_node])
        # stack not empty, pop FIFO item
        while s.size() > 0:
            path = s.pop()
            v = path[-1]

            # if that vertex has not been visited, marked it as visited
            if v not in visited:
                visited.add(v)
                # add more ancestor to ancestor tree
                if len(final_path) < len(path) :
                    final_path = path.copy()
                # child has two ancestors, choose smaller ancestor
                elif len(final_path) == len(path) and final_path > path :   # [8,11] > [8,4], final_path=[8,4]
                    final_path = path.copy()
                # then get all path leading its neighbor onto stack
                for neighbor in self.vertices[v]:
                    # create new path to its neighbor
                    path_copy = path.copy()     # list(path) equivalent
                    # attach vertex neighbor to end of path
                    path_copy.append(neighbor)
                    # push onto stack to be looped
                    s.push(path_copy)


        if final_path == [starting_node]:
            return(-1)
        else:        
            return(final_path[-1])  # return earliest ancestor

    

def earliest_ancestor(relation, starting_child):

    graph = Graph()
    for parent, child in relation:
        graph.add_vertex(parent)
        graph.add_vertex(child)

    for parent, child in relation:
        graph.add_edge(child, parent)

    #print(list(graph.vertices[3]))
    return(graph.dft(starting_child))
    
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors,6))
