# dfs
class Solution:
    def isBipartite(self, g):
        v=[-1]*len(g)
        def dfs(n,c): 
            for i in g[n]:
                x=0 if c==1 else 1
                if v[i]==c:
                    return False
                if v[i]==-1:
                    v[i]=x
                    if not dfs(i,x):
                        return False
            return True
        for k in range(len(g)):
            if v[k]==-1:
                v[k]=1
                if not dfs(k,1):
                    return False
        return True
                
                
                


        