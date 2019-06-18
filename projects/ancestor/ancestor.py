from utils.py import Stack, Queue

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        if v1 in self_vertices and v2 in self.vertices :
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Either vertex {v1} or {v2} does not exist.")
            
    def dft(self, starting_vertex, destination_vertex):
        # create an empty set to store visited nodes
        visited = set()
        # create a empty stack and push starting vertex path
        s = Stack() 
        s.push( [starting_vertex])
        # stack not empty, pop FIFO item
        while s.size() > 0:
            path = s.pop()
            # check whether current vertex of a path has reached its the target vertex
            v = path[-1]
            if v == destination_vertex :
                return(f'child to parent = {path}')
            # if that vertex has not been visited, marked it as visited
            if v not in visited:
                visited.add(v)
                # then get all path leading its neighbor onto stack
                for neighbor in self.vertices[v]:
                    # create new path to its neighbor
                    path_copy = path.copy()     # list(path) equivalent
                    # attach vertex neighbor to end of path
                    path_copy.append(neighbor)
                    # push onto stack to be looped
                    s.push(path_copy)

        