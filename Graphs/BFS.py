# TC- o(V+E)
# SC - O(V)
def BFS(v,e,s):
    q=[s]
    v=[False]*v
    v[s]=True
    ans=[]
    while q:
        x=q.pop(0)
        ans.append(x)
        y=e[x]
        for i in y:
            if not v[i]:
                v[i]=True
                q.append(i)
    return ans
        

