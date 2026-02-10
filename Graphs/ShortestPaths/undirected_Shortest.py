# basic BFS
class Solution:
    def shortestPath(self, V, edges, src):
        # code here
        g=[[] for i in range(V)]
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
        ans=[-1]*V
        q=[src]
        l=0
        v=[False]*V
        v[src]=True
        while q:
            n=len(q)
            for i in range(n):
                x=q.pop(0)
                ans[x]=l
                for nei in g[x]:
                    if not v[nei]:
                        v[nei]=True
                        q.append(nei)
            l+=1
        return ans