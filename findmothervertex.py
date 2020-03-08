from collections import defaultdict
class Graph :
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def dfs(self,i,visited):
        visited[i]=True
        for j in self.graph[i]:
            if visited[j]==False:
                self.dfs(j,visited)
        
    def mother(self):
        visited=[False]*self.V 
        v=0
        for i in range(self.V):
            if visited[i]==False:
                self.dfs(i,visited)
                v=i
        visited=[False]*self.V 
        self.dfs(v,visited)
        if any(i==False for i in visited):
            return -1
        else:
            return v

g=Graph(5)
g.addEdge(0,1)
g.addEdge(0,4)
g.addEdge(0,2)
g.addEdge(2,1)
g.addEdge(2,3)
g.addEdge(3,4)
print("mother vertex is :",g.motther())