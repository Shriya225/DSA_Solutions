# khans algo
# reverse graph
# all paths from outdegree leads to all possible ans
# rest can never be answers
class Solution:
    def eventualSafeNodes(self, g):
        ng=[[] for i in range(len(g))]
        deg=[0]*len(g)
        for i in range(len(g)):
            for x in g[i]:
                ng[x].append(i)
                deg[i]+=1
        ans=[]
        q=[i for i in range(len(deg)) if deg[i]==0]
        while q:
            x=q.pop(0)
            ans.append(x)
            for nei in ng[x]:
                deg[nei]-=1
                if deg[nei]==0:
                    q.append(nei)
        return sorted(ans)
            
        
