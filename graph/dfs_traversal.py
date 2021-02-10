
def dfs(graph, start, visited=[]):
    print (start)
    visited.append(start)
    neigh = graph[start]
    for new_start in neigh:
        if new_start in visited:
            continue
        else:
            visited.append(new_start)
            dfs(graph, new_start, visited)
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

dfs(graph, '0')
