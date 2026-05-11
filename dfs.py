graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
 
visited = set()
stack = []
start = 'A'
stack.append(start)
 
print("DFS Traversal:")
 
while stack:
    node = stack.pop()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in reversed(graph[node]):
            stack.append(neighbour)
 
