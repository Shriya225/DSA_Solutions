# use khans algo
# topo sort
class Solution:
    def topoSort(self, V, edges):
        v=[0]*V
        g=[[] for i in range(V)]
        for x,y in edges:
            v[y]+=1
            g[x].append(y)
        q=[]
        ans=[]
        for i in range(V):
            if v[i]==0:
                ans.append(i)
                q.append(i)
        while q:
            x=q.pop(0)
            for i in g[x]:
                if v[i]>0:
                    v[i]-=1
                    if v[i]==0:
                        ans.append(i)
                        q.append(i)
        if len(ans)!=V:
            return False
        return True