class UnDirectedGraph:
    def __init__(self, n):
        self.n = n

    def adjacency_dict(self, edges):
        adj_list_dict = {}  
        for pair in edges:
            u,v = pair
            if u not in adj_list_dict:
                adj_list_dict[u] = []
            if v not in adj_list_dict:
                adj_list_dict[v] = []
            adj_list_dict[u].append(v)
            adj_list_dict[v].append(u)  
        return adj_list_dict


    def adjacency_array(self, edges):
        adj_list_array = [[] for _ in range(self.n + 1)]  
        for pair in edges:
            u,v = pair 
            adj_list_array[u].append(v)
            adj_list_array[v].append(u)  
        return adj_list_array
    

class DirectedGraph:
    def __init__(self, n):
        self.n = n

    def adjacency_dict(self, edges):
        adj_list_dict = {}  

        for pair in edges:
            u,v = pair
            if u not in adj_list_dict:
                adj_list_dict[u] = []
            adj_list_dict[u].append(v)

        return adj_list_dict


    def adjacency_array(self, edges):
        adj_list_array = [[] for _ in range(self.n + 1)]  
        for pair in edges:
            u,v = pair 
            adj_list_array[u].append(v)
        return adj_list_array


n = 5 
edges = [(1, 2), (1, 3), (2, 4), (3, 5)]

graph1 = UnDirectedGraph(n)
graph2 = DirectedGraph(n)

adj_dict = graph1.adjacency_dict(edges)
print("Adjacency List (Dictionary):")
for node, neighbors in adj_dict.items():
    print(f"{node}: {neighbors}")


adj_array = graph1.adjacency_array(edges)
print("\nAdjacency List (Array):")
for node in range(1, n + 1): 
    print(f"{node}: {adj_array[node]}")

adj_dict = graph2.adjacency_dict(edges)
print("\nAdjacency List (Dictionary):")
for node, neighbors in adj_dict.items():
    print(f"{node}: {neighbors}")

adj_array = graph2.adjacency_array(edges)
print("\nAdjacency List (Array):")
for node in range(1, n + 1): 
    print(f"{node}: {adj_array[node]}")
