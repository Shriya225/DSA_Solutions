# 547. Number of Provinces
# using DFS
def cc(V,e,g):
    v=[False]*V
    # do dfs
    def dfs(g,s):
        v[s]=True
        for i in range(V):
            if g[s][i]==1 and not v[i]:
                dfs(g,i)
    ans=0
    for i in range(V):  
        if not v[i]:
            ans+=1
            dfs(g,i)
    return ans
