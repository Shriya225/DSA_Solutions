# start from souce
# relaxedges...ift ehy give beter ans stroe in pq
# process from min ...
# then check if already exisiting path or new one gives better tehn move ahead
# normal dij ..just add the concept of edge wt is diff of ees not wt sum.
import heapq
class Solution:
    def minimumEffortPath(self, g):
        pq=[]
        ans=[[float('inf')]*len(g[0]) for i in range(len(g))]
        ans[0][0]=0
        heapq.heappush(pq,(0,(0,0)))
        while pq:
            k,t=heapq.heappop(pq)
            x,y=t
            d=[[0,1],[0,-1],[1,0],[-1,0]]
            for i,j in d:
                if 0<=x+i<len(g) and 0<=y+j<len(g[0]):
                    z=max(k,abs(g[x][y]-g[x+i][y+j]))
                    if ans[x+i][y+j]>z:
                        ans[x+i][y+j]=z
                        heapq.heappush(pq,(z,(x+i,y+j)))
        return ans[-1][-1] if ans[-1][-1]!=float('inf') else -1

