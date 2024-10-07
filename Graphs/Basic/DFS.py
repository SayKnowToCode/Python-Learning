class DFS:
    def DFSList(self, graph, start):
        dfs = []
        visited = [False] * (len(graph) + 1)

        def dfs_util(node):
            visited[node] = True
            dfs.append(node)

            for neighbour in graph[node]:
                if visited[neighbour] == False:
                    dfs_util(neighbour)

        dfs_util(start)
        return dfs
    
    def DFSMatrix(self, graph, start):
        dfs = []
        visited = [False] * (len(graph) + 1)

        def dfs_util(node):
            visited[node] = True
            dfs.append(node)

            for j in range(len(graph[node])):
                if graph[node][j] == 1 and visited[j] == False:
                    dfs_util(j)
                    
        dfs_util(start)
        return dfs
    
adj_list = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3, 11],
    8: [4],
    9: [5],
    10: [6],
    11: [7]
}

adj_matrix = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],  
    [ 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0 ],  
    [ 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ],  
    [ 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0 ],  
    [ 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0 ],  
    [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0 ],  
    [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1 ],  
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 ],  
    [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0 ],  
    [ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ],  
    [ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],  
]

dfs = DFS()
print(dfs.DFSList(adj_list, 1))
print(dfs.DFSMatrix(adj_matrix, 1))

print(dfs.DFSList(adj_list, 6))
print(dfs.DFSMatrix(adj_matrix, 6))