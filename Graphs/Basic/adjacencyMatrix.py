class UnDirectedGraph:
    def __init__(self,n):
        self.n = n

    def adjacency_matrix(self, edges):
        matrix = [[0 for _ in range(self.n + 1)] for _ in range(self.n + 1)]
        for u,v in edges:
            matrix[u][v] = 1
            matrix[v][u] = 1
        return matrix
    
class DirectedGraph:
    def __init__(self,n):
        self.n = n

    def adjacency_matrix(self, edges):
        matrix = [[0 for _ in range(self.n + 1)] for _ in range(self.n + 1)]
        for u,v in edges:
            matrix[u][v] = 1
        return matrix


n = 5 
edges = [(1, 2), (1, 3), (2, 4), (3, 5)]

graph1 = UnDirectedGraph(n)
graph2 = DirectedGraph(n)

matrix1 = graph1.adjacency_matrix(edges)
matrix2 = graph2.adjacency_matrix(edges)

print(matrix1)
print()
print(matrix2)
