# 743. Network Delay Time
# dij algo
import heapq
class Solution:
    def networkDelayTime(self, e, V: int, k: int) -> int:
        g=[[] for _ in range(V)]
        for x,y,z in e:
            g[x].append([y,z])
        pq=[]
        ans=[float('inf')]*V
        heapq.heappush(pq,(0,k))
        while pq:
            wt,p=heapq.heappop(pq)
            if ans[p]<wt:
                continue
            for n,nwt in g[p]:
                if wt+nwt <ans[n]:
                    ans[n]=wt+nwt
                    heapq.heappush(pq,(wt+nwt,n))
        min_ans=float('inf')
        for i in ans:
            if i==float('inf'):
                return -1
            min_ans=min(min_ans,i)
        return min_ans
        
