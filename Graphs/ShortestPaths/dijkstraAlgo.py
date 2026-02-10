# DAG shortest path → relax edges in topological order
# Dijkstra → relax edges by minimum distance using priority queue
# dijktra -- greeedy (go to min on pq to get min path)
import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        g=[[] for i in range(V)]
        for x,y,z in edges:
            g[x].append([y,z])
            g[y].append([x,z])
        pq=[]
        ans=[float('inf')]*V
        ans[src]=0
        heapq.heappush(pq,(0,src))
        while pq:
            d,p=heapq.heappop(pq)
            if d>ans[p]:
                continue
            for n,wt in g[p]:
                if d+wt<ans[n]:
                    ans[n]=d+wt
                    heapq.heappush(pq,(d+wt,n))
        return ans