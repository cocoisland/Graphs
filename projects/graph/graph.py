"""
Simple graph implementation
"""
from graph.util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices :
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Either {v1} or {v2} vertices does no exist.")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty set to store visited nodes
        visited = set()
        # Create an empty Queue and enqueue the starting vertex
        q = Queue()
        q.enqueue(starting_vertex)
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                print(f'bft print {v}')
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        s = Stack()
        s.push(starting_vertex)
        while s.size() > 0 :
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(f'dft print {v}')
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
        
            for neighbor in self.vertices[starting_vertex]:
                self.dft_recursive(neighbor, visited)

        '''
        visited = set()
        def inner_recursive(vertex):
            if vertex in visited:
                print(f' never print because starting vertex is not visited but immediately added.')
                return
            print(f'DFS recursive vertex {vertex}')
            visited.add(vertex)
            for neighbor in self.vertices[vertex]:
                if neighbor not in visited:
                    inner_recursive(neighbor)
        inner_recursive(starting_vertex)
        '''

        # print(f'dft recursive')
        # visited = set()
        # def inner_recursive(vertex):
        #     visited.add(vertex)
        #     
        #     print(f'Recursive vertex = {vertex} {visited}')
        #     for neighbor in self.vertices[vertex]:
        #         if neighbor not in visited:
        #             inner_recursive(neighbor)

        #     print(f' Nothing printed from {visited} because this visited is not part of recursive loop.')
  


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty set to store visited nodes
        visited = set()
        # Create an empty Queue and enqueue A PATH TO the starting vertex
        q = Queue()
        path = [starting_vertex]
        q.enqueue(path)
        # While the queue is not empty...
        while q.size() > 0 :
            # Dequeue the first PATH
            path = q.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = path[-1]
            # IF VERTEX = TARGET, RETURN PATH
            if v == destination_vertex :
                return(f'BFS shortest path {path}')
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Then add A PATH TO all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    # Copy the path
                    path_copy = path.copy()
                    # Append neighbor to the back of the copy
                    path_copy.append(neighbor)
                    # Enqueue copy
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        s = Stack()
        path = [starting_vertex]
        s.push(path)
        while s.size() > 0:
            path = s.pop()
            v = path[-1]
            if v == destination_vertex :
                return(f'DFS shortest path {path}')
            
            if v not in visited:
                visited.add(v)
                for neighbor in self.vertices[v]:
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    s.push(path_copy)





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    #print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    #graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    #graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    #graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    #print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
