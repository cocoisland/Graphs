'''
Write a function that takes a 2D binary array and
returns the number of 1 islands. An island consists
of 1s that are connected to the north, south, east
or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4
'''

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 0, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 1, 1]]

# islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
#            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
#            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
#            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
#            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
#            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
#            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
#            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
#            [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
#            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]



# 1. Translate problem into graph terminology:
'''
Understand the problem:
1. An island is made up of at least 3 ones' located in 3 of the 4 direction(n,s,w,e).
Island boundary is marked by 0 or matrix edge.
Is a graph problem because of keyword "connected" to north, south, west or east.

2. Build a graph based on "connected" to north, south, west, or east.

3. Traverse graph checking for connection to north, south, west or east.
'''



# 2. Build your graph

def get_neighbors(v, matrix):
    col = v[0]
    row = v[1]
    neighbors = []
    # Check North
    if row > 0 and matrix[row - 1][col] == 1:
        neighbors.append((col, row-1))
    # Check South
    if row < len(matrix) - 1 and matrix[row + 1][col] == 1:
        neighbors.append((col, row+1))
    # Check East
    if col < len(matrix[0]) - 1 and matrix[row][col + 1]:
        neighbors.append((col + 1, row))
    # Check West
    if col > 0 and matrix[row][col - 1]:
        neighbors.append((col - 1, row))
    return neighbors




# 3. Traverse your graph

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


def island_counter(matrix):
    # DFS - traverse vertically by each row first, then horizontally by column
    # Create a visited matrix
    visited = []
    for i in range(len(matrix)): # number of rows in 2x2 matrix
        visited.append([False] * len(matrix[0])) # number of columns in 2x2 matrix
    island_count = 0
    # Walk through each cel in the matrix
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            # If that cel has not been visited
            if not visited[row][col]:
                # When I reach a 1,
                if matrix[row][col] == 1:
                    # Do a DFT and mark each as visited
                    visited = dft(col, row, matrix, visited)
                    # Then increment the counter by 1
                    island_count += 1
    # Return island count
    return island_count

def island_counter_BFS(matrix):
    # BFS - traverse horizontal by each column first, then vertically by row
    # Create a visited matrix
    visited = []
    for i in range(len(matrix)): # number of rows in 2x2 matrix
        visited.append([False] * len(matrix[0])) # number of columns in 2x2 matrix
    island_count=0
    # Walk through each cel in the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            # If that cel has not been visited
            if not visited[row][col]:
                # When I reach a 1,
                if matrix[row][col] == 1:
                    # Do a BFT and mark each as visited
                    visited = bft(col, row, matrix, visited)
                    # Then increment the counter by 1
                    island_count += 1

    # Return island count
    return island_count

def dft(col, row, matrix, visited):
    s = Stack()
    s.push((col, row))
    while s.size() > 0:
        v = s.pop()
        col = v[0]
        row = v[1]
        if not visited[row][col]:
            visited[row][col] = True
            for neighbor in get_neighbors(v, matrix):  # STUB
                s.push(neighbor)
    return visited


def bft(col, row, matrix, visited):
    s = Queue()
    s.enqueue((col, row))
    while s.size() > 0:
        v = s.dequeue()
        col = v[0]
        row = v[1]
        if not visited[row][col]:
            visited[row][col] = True
            for neighbor in get_neighbors(v, matrix):  # STUB
                s.enqueue(neighbor)
    return visited



print(f' DFS-traverse vertically row, then horizontally column = {island_counter(islands)}')
print(f' BFS-traverse horizontally column, then vertically row = {island_counter_BFS(islands)}')