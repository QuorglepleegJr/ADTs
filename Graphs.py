class Graph():

    def from_console():

        num = int(input("Enter number of vertices: "))

        edges = set()
        
        for x in range(int(input("Enter number of edges: "))):

            a = int(input(f"Edge {x+1} Start: "))
            b = int(input(f"Edge {x+1} End: "))

            edges.add((a,b))
        
        return Graph(num, *edges)
    
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

        pass
    
    def print_matrix(self):

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
    
    def print_list(self):

        pass

g = Graph.from_console()

g.print_matrix()