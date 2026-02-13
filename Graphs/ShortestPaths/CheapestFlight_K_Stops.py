#modified dij
# 787. Cheapest Flights Within K Stops
import heapq
class Solution:
    def findCheapestPrice(self, V: int, f, src: int, dst: int, stops: int) -> int:
        g=[[] for i in range(V)]
        for x,y,z in f:
            g[x].append([y,z])
        
        def dij(g):
            ans=[[float("inf")]*(stops+2) for i in range(V)]
            ans[src][0]=0
            pq=[]
            heapq.heappush(pq,(0,src,0))
            while pq:
                wt,p,k=heapq.heappop(pq)
                if p==dst and k<=stops+1:
                                return wt
                if k+1<=stops+1:
                    for n,nwt in g[p]:
                        if wt+nwt<ans[n][k+1]:
                            ans[n][k+1]=wt+nwt
                            heapq.heappush(pq,(wt+nwt,n,k+1))
            return -1
        return dij(g)
                
                
                    

