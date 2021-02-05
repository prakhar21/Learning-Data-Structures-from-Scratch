class Graph:
    def __init__(self, num_nodes):
        self.num_nodes=num_nodes
        self.adj_mat=[[0]*self.num_nodes for i in range(num_nodes)]
    
    def add_edge(self, v1, v2):
        if v1==v2: print ("Same Nodes")
        self.adj_mat[v1][v2]=1
        self.adj_mat[v2][v1]=1
    
    def delete_edge(self, v1, v2):
        if v1==v2: return "Same nodes, can't be deleted"
        self.adj_mat[v1][v2]=0
        self.adj_mat[v2][v1]=0
    
    def print_adj(self):
        for row in self.adj_mat:
            print (row)
    
g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.print_adj()
print ('-'*10)
g.delete_edge(0, 1)
g.print_adj()
