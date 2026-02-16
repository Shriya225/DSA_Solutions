
import heapq
class Solution:
    def spanningTree(self, V, edges):
        g=[[] for i in range(V)]
        for x,y,z in edges:
            g[x].append([y,z])
            g[y].append([x,z])
        pq=[]
        ans=0
        vis=[False]*V
        heapq.heappush(pq,(0,0))
        while pq:
            w,p=heapq.heappop(pq)
            # if u dont add this/
            # code will fail on this
            #       2
            #    0 ---- 1
            #    |      /
            #  1 |    3
            #    |   /
            #    2
            # Do a dry run and check it out.
            if vis[p]:
                continue
            ans+=w
            vis[p]=True
            for n,nwt in g[p]:
                if not vis[n]:
                    heapq.heappush(pq,(nwt,n))
        return ans

        
           
           