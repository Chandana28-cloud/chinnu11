from collections import defaultdict
class Graph :
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def sumOfDependies(self):
        sum=0
        for i in range(self.V):
            sum=sum+len(self.graph[i])
        return sum    
        
vertices=int(input("enter no of vertices"))
edge=int(input("enter no of edges"))
g=Graph(vertices)
for i in range(edge):
    u,v=int(input("from")),int(input("to"))
    g.addEdge(u,v)
print("sum of dependies :",g.sumOfDependies())
