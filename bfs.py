graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}
 
visited = set()
queue = []
start = 'A'
 
queue.append(start)
 
print("BFS Traversal")
 
while queue:
    node = queue.pop(0)
 
    if node not in visited:
        print(node, end=" ")
 
        visited.add(node)
 
        for neighbour in graph[node]:
            queue.append(neighbour)
