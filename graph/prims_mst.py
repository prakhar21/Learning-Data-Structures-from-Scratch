def prims_mst(graph, start_node):
    visited = [start_node]
    while len(visited) != len(graph[0]):
        start = graph[start_node]
        minimum = 100000
        minimum_idx = -1
        for idx, val in enumerate(start):
            if minimum >= val and idx!=start_node and val!=0 and idx not in visited:
                minimum = val
                minimum_idx = idx
        
        start_node = minimum_idx
        visited.append(minimum_idx)
    return visited

graph = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

start_node=0
print (prims_mst(graph, start_node))
