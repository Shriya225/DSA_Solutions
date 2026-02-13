# Dijkstra
MOD = 10**9 + 7
import heapq
class Solution:
    def countPaths(self, V: int, e) -> int:
        g=[[] for i in range(V)]
        for x,y,z in e:
            g[x].append([y,z])
            g[y].append([x,z])
        pq=[]
        ans=[float('inf')]*V
        ans[0]=0
        ways=[0]*V
        ways[0]=1
        heapq.heappush(pq,(0,0))
        while pq:
            wt,p=heapq.heappop(pq)
            if wt>ans[p]:continue
            for n,nwt in g[p]:
                if wt+nwt<ans[n]:
                    ans[n]=wt+nwt
                    ways[n]=ways[p]
                    heapq.heappush(pq,(wt+nwt,n))
                elif wt+nwt==ans[n]:
                    ways[n] = (ways[n] + ways[p]) % MOD
        return ways[-1]


