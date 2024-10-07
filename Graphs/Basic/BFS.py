class BFS:
    def BFSList(self, graph, start):
        visited = [False] * (len(graph) + 1)
        visited[start] = True
        queue = []
        queue.append(start)
        bfs = []

        while queue:
            node = queue.pop(0)
            bfs.append(node)

            for neighbour in graph[node]:
                if visited[neighbour] == False:
                    visited[neighbour] = True
                    queue.append(neighbour)
        
        return bfs
    
    def BFSMatrix(self, graph, start):
        visited = [False] * (len(graph) + 1)
        visited[start] = True
        queue = []
        queue.append(start)
        bfs = []

        while queue:
            node = queue.pop(0)
            bfs.append(node)

            for j in range(len(graph[node])): 
                if graph[node][j] == 1 and visited[j] == False:
                    visited[j] = True
                    queue.append(j)

        return bfs
    
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
    # 0  1  2  3  4  5  6  7  8  9 10 11 (Nodes)
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],  # Node 0 (Not used)
    [ 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],  # Node 1
    [ 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0 ],  # Node 2
    [ 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ],  # Node 3
    [ 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0 ],  # Node 4
    [ 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0 ],  # Node 5
    [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0 ],  # Node 6
    [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1 ],  # Node 7
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 ],  # Node 8
    [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0 ],  # Node 9
    [ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ],  # Node 10
    [ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],  # Node 11
]


bfs = BFS()
print(bfs.BFSList(adj_list, 1))
print(bfs.BFSMatrix(adj_matrix, 1))

print(bfs.BFSList(adj_list, 6))
print(bfs.BFSMatrix(adj_matrix, 6))