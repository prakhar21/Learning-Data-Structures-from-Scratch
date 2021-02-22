def prims_mst(graph, start_node):
    nodes_order=[]
    visited = [False]*len(graph[0])
    visited[start_node] = True
    nodes_order.append(start_node)
    while len(nodes_order) != len(graph[0]):
        minimum = 100000
        x, y = None, None
        for start in range(len(graph[0])):
            if visited[start]:
                for end in range(len(graph[0])):
                    if start!=end and graph[start][end]!=0 and visited[end]==False:
                        if minimum >= graph[start][end]:
                            minimum = graph[start][end]
                            x=start
                            y = end
        
        print (x, y)
        visited[y]=True
        nodes_order.append(y)

graph = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

start_node=0
prims_mst(graph, start_node)
