# GFG
# Connected Components in an Undirected Graph

# using BFS
def ConnecetdOComponents(g):
    v=[False]*len(g)
    ans=[]
    for i in range(len(g)):
        if not v[i]:
            q=[i]
            v[i]=True
            l=[]
            while q:
                    x=q.pop(0)
                    l.append(x)
                    y=g[x]
                    for e in y:
                        if not v[e]:
                            q.append(e)
                            v[e]=True
            ans.append(l)
    return ans

# using DFS
def cc(V,e):
    #  create adjacency list 1st
    g=[[] for i in range(V)]
    for u,v in e:
          g[u].append(v)
          g[v].append(u)
    
    v=[False]*V
    # do dfs
    def dfs(g,s):
        l.append(s)
        v[s]=True
        for e in g[s]:
            if not v[e]:
                dfs(g,e)
    ans=[]
    for i in range(V):  
        if not v[i]:
            l=[] 
            dfs(g,i)
            ans.append(l)  

 
        
        
         
         
         