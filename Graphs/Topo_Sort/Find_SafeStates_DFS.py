# DFS
# Detect cyle, eles that are directing to cylce are not safe nodes
# rest are safe.
# GFG

#  this soln uses, Vis array,path arr,ans arr
class Solution:
    def safeNodes(self, V, edges):
        g=[[] for i in range(V)]
        for x,y in edges:
            g[x].append(y)
        v=[False]*V
        p=[False]*V
        ans=[0]*V
        
        def dfs(n):
            # what if i vist unsafe declred node agin. I dont wnat to do dfs agin ..waste of time
            if ans[n]==-1:
                return False
            # what if i went ot safe node agin ,to stop dfs agin
            if ans[n]==1:
                return True
            if v[n] and p[n]:
                ans[n]=-1
                return False
            v[n]=True
            p[n]=True
            for i in g[n]:
                    if not dfs(i):
                        ans[n]=-1
                        return False
            p[n]=False
            ans[n]=1
            return True
        for i in range(V):
            if not v[i]:
                if not dfs(i):
                    ans[i]=-1
        ans2=[]
        for i in range(V):
            if ans[i]==1:
                ans2.append(i)
        return ans2


