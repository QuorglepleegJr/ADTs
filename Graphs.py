from Queues import LinearQueue
from math import inf

class Graph():

    def from_console():

        # Takes input for directed, add both directions for undirected

        num = int(input("Enter number of vertices: "))

        edges = set()
        
        edge_no = int(input("Enter number of edges: "))

        if edge_no >= num * (num-1):

            print("Creating complete graph")

            return Graph.new_complete(num)

        for x in range(edge_no):

            a = int(input(f"Edge {x+1} Start: "))
            b = int(input(f"Edge {x+1} End: "))

            edges.add((a,b))
        
        return Graph(num, *edges)

    def new_complete(n):

        edges = {(a,b) for a in range(n) for b in range(n) if a != b}

        return Graph(n, *edges)
    
    def __init__(self, num_vertices, *edges):
        
        self.__num_vertices = num_vertices
        self.__edges = set(edges)
    
    def bfs(self, start=0):

        adj_list = self.adj_list()

        visit_q = LinearQueue(self.__num_vertices)
        visited = [start]
        distances = [inf] * self.__num_vertices
        distances[start] = 0
        parents = [None] * self.__num_vertices

        visit_q.enqueue(start)

        while not visit_q.is_empty():

            current = visit_q.dequeue()

            for other in adj_list[current]:
                
                if not other in visited:

                    visited.append(other)
                    visit_q.enqueue(other)
                    distances[other] = distances[current] + 1
                    parents[other] = current
        
        return visited, distances, parents

    def matrix(self):

        m = [[0]*self.__num_vertices for _ in range(self.__num_vertices)]

        for edge in self.__edges:

            m[edge[0]][edge[1]] = 1
        
        return m

    def adj_list(self):

        l = [[] for _ in range(self.__num_vertices)]

        for edge in self.__edges:

            l[edge[0]].append(edge[1])
        
        for connections in l:

            connections.sort()
        
        return l
    
    def print_matrix(self):

        print("\nMatrix:\n")

        print(" "+" "*len(str(self.__num_vertices))+"| ", end="")

        for x in range(self.__num_vertices):

            print(str(x)+" ", \
                end=" "*(len(str(self.__num_vertices))-len(str(x))))
        
        print("\n"+"-"*((len(str(self.__num_vertices))+1)*self.__num_vertices+3))

        for index, row in enumerate(self.matrix()):

            print(str(index)+" "*(len(str(self.__num_vertices))-len(str(index)))\
                  + " | ", end="")
            
            for item in row:
                
                print(str(item)+" "*(len(str(self.__num_vertices))), end="")
            
            print()
        
        print("\n")
    
    def print_list(self):

        print("\nList:\n")

        for index, connections in enumerate(self.adj_list()):

            print(str(index) + " "*(len(str(self.__num_vertices)) \
                - len(str(index))) + " | ", end="")
            print(*connections, sep=", ")
        
        print("\n")
    
    def print_bfs_order(self, start=0):

        visited = self.bfs(start)[0]

        print(", ".join([str(n) for n in visited]))
    
    def __printless_get_shortest_path(self, start, end):

        distances, parents = self.bfs(start)[1:]

        if distances[end] == inf: return None

        path = [end]

        current = end

        while parents[current] is not None:
            
            current = parents[current]

            path = [current] + path
        
        return distances[end], path

    def get_shortest_path(self, start=0, end=1):

        shortest_path = self.__printless_get_shortest_path(start, end)

        if shortest_path is None:

            print(f"No path exists between {start} and {end}")
            print()

        print(f"Shortest path between {start} and {end}:")
        print(f"Length {shortest_path[0]}")
        print(" -> ".join([str(n) for n in shortest_path[1]]))
        print()

        return shortest_path
    
    def get_all_shortest_paths(self, start=0):

        print(f"\nAll shortest paths from {start}:\n")

        distances, parents = self.bfs(start)[1:]

        paths = []

        for end in range(self.__num_vertices):

            if end != start:

                if distances[end] != inf:

                    path = [end]

                    current = end

                    while parents[current] is not None:
            
                        current = parents[current]

                        path = [current] + path

                    print(f"{end} | {distances[end]} | " + \
                        " -> ".join([str(n) for n in path]))
                    
                    paths.append((end, distances[end], path))
                
                else:

                    print(f"{end} | No path")
                    paths.append((end, None))
        
        print()

        return paths

        

        
                

g = Graph.from_console()

g.print_matrix()

g.get_all_shortest_paths()