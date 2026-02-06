# TC- o(V+E)
# SC - O(V)
def DFS_g(g):
    v=[False]*len(g)
    ans=[]
    def dfs(g,s):
        nonlocal v
        ans.append(s)
        v[s]=True
        if not g[s]:
            return
        for e in g[s]:
            if not v[e]:
                dfs(g,e)
    dfs(g,0)
    return ans
    