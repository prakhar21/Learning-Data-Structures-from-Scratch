from collections import deque 
de = deque([])

def bfs(graph, current, visited=[]):
    global de
    
    print (current)
    visited.append(current)
    
    for n in graph[current]:
        de.append(n)
    
    while len(de):
        current = de.popleft()
        if current not in visited:
            bfs(graph, current, visited)
    return

graph = {
    '0': ['1', '2'],
    '1': ['0', '3', '4'],
    '2': ['0'],
    '3': ['1'],
    '4': ['1', '2', '3', '5'],
    '5': ['4']
    }

# 0 - 1 - 3
# |   | /
# 2 - 4 - 5

bfs(graph, '0')

