# gfg
# DFS
# use path arr,vis arr
class Solution:
    def isCyclic(self, V, edges):
        # code here
        g=[[] for _ in range(V)]
        for x,y in edges:
            g[x].append(y)

        v=[False]*V
        p=[False]*V
        def dfs(n):
            v[n]=True
            p[n]=True
            for i in g[n]:
                if not v[i]:
                    if dfs(i):
                        return True
                elif p[i]:
                    return True
            p[n]=False
            return False
        for k in range(len(g)):
            if not v[k]:
                if dfs(k):
                    return True
        return False