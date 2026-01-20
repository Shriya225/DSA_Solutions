# 733. Flood Fill
# dfs
class Solution:
    def floodFill(self, g, sr: int, sc: int, c: int):
        x=g[sr][sc]
        def dfs(g,s,e):
            # to avoid infinite recursion
            if x==c:
                return
            if (s<0 or s==len(g)) or (e<0 or e==len(g[0])):
                return
            if g[s][e]!=x:
                return
            g[s][e]=c
            dfs(g,s+1,e)
            dfs(g,s-1,e)
            dfs(g,s,e+1)
            dfs(g,s,e-1)
        dfs(g,sr,sc)
        return g