from Queues import LinearQueue
from Stacks import Stack
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
        visit_q.enqueue(start)
        visited = [start]
        distances = [inf] * self.__num_vertices
        distances[start] = 0
        parents = [None] * self.__num_vertices


        while not visit_q.is_empty():

            current = visit_q.dequeue()

            for other in adj_list[current]:
                
                if not other in visited:

                    visited.append(other)
                    visit_q.enqueue(other)
                    distances[other] = distances[current] + 1
                    parents[other] = current
        
        return visited, distances, parents
    
    def dfs(self, start=0):

        adj_list = self.adj_list()

        visit_stack = Stack()
        visit_stack.push(start)
        visited = []
        starts = [None] * self.__num_vertices
        ends = [None] * self.__num_vertices
        parents = [None] * self.__num_vertices

        counter = 0

        self.print_list()

        while not visit_stack.is_empty():

            current = visit_stack.pop()

            if current not in visited:

                starts[current] = counter
                counter += 1

                visited.append(current)

                others = [x for x in adj_list[current] if x not in visited]
                
                for i in range(len(others)-1, -1, -1):

                    visit_stack.push(others[i])
                    parents[others[i]] = current
                
                if len(others) == 0:
                
                    parent = parents[current]
                    child = current

                    ends[current] = counter
                    counter += 1
                    
                    while parent is not None:
                        
                        for p in adj_list[child]:

                            print(child, p, adj_list)

                            if len(adj_list[p]) > 0 and child == adj_list[p][-1]:

                                adj_list[p].pop()
                            
                            elif len(adj_list[p]) > 0:

                                if p == parent:

                                    break

                        ends[parent] = counter
                        counter += 1

                        child = parent
                        parent = parents[child]
                        
        
        return visited, starts, ends, parents

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

        print("Matrix:\n")

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

        print("List:\n")

        for index, connections in enumerate(self.adj_list()):

            print(str(index) + " "*(len(str(self.__num_vertices)) \
                - len(str(index))) + " | ", end="")
            print(*connections, sep=", ")
        
        print("\n")
    
    def print_bfs_order(self, start=0):

        visited = self.bfs(start)[0]

        print(", ".join([str(n) for n in visited]))
    
    def get_shortest_path(self, start=0, end=1):

        distances, parents = self.bfs(start)

        if distances[end] == inf:

            return inf, []

        path = []

        current = end

        while parents[current] is not None:

            path = [current] + path
            
            current = parents[current]
    
        return distances[end], path

    def print_shortest_path(self, start=0, end=1):

        distance, path = self.get_shortest_path(start, end)

        if distance == inf:

            print(f"No path exists between {start} and {end}")
            print()

        else:

            print(f"Shortest path between {start} and {end}:")
            print(f"Length {distance}")
            print(" -> ".join([str(n) for n in path]))
            print()
    
    def get_all_shortests_to_node(self, start=0):

        pass

    


g = Graph.from_console()

print(g.dfs())