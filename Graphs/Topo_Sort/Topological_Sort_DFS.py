# post order traversal + stk rev gves aswer
# this works only fr DAG
# if not it gives wrong answers. so being a DAG is must
class Solution:
    def topoSort(self, V, edges):
        g=[[] for _ in range(V)]
        for x,y in edges:
            g[x].append(y)
        
        v=[False]*V
        ans=[]
        def dfs(n):
            for k in g[n]:
                if not v[k]:
                    v[k]=True
                    dfs(k)
            ans.append(n)

        for i in range(V):
            if not v[i]:
                v[i]=True
                dfs(i)
        return ans[::-1]
        