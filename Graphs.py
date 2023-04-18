class Graph():

    def from_console():

        num = int(input("Enter number of vertices: "))

        edges = set()
        
        edge_no = int(input("Enter number of edges: "))

        if edge_no == num * (num-1):

            print("Creating complete graph")

            return Graph.new_complete(num)

        for x in range():

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

g = Graph.from_console()

g.print_list()
g.print_matrix()