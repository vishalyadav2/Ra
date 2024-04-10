from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ') 
            visited.add(node)
            queue.extend(graph[node] - visited)

graph = {
    '1': {'2', '3'},
    '2': {'1', '6', '7'},
    '3': {'1', '4', '5'},
    '4': {'3'},
    '5': {'3'},
    '6': {'2'},
    '7': {'2','8'},
    '8': {'7'}
}

bfs(graph, '1')
print("is the Breadth-First Search")
