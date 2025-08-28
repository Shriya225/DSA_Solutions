import heapq
def dijkstars(a,s):
    ans=[float("inf")]*(len(a))
    ans[s]=0
    pq=[]
    heapq.heappush(pq,(0,s))
    while pq:
        dist,n=heapq.heappop(pq)
        for adjNode,wt in a[n]:
            if dist+wt<ans[adjNode]:
                ans[adjNode]=dist+wt
                heapq.heappush(pq,(dist+wt,adjNode))
    return ans
adj = [ [(1,1), (2,4)],  
       [(0,1), (2,2)], 
         [(0,4), (1,2)] ]
ans=dijkstars(adj,0)
print(f"Shortest distances from node {0}:")
for i in range(len(adj)): 
    print(f"Node {i} -> {ans[i]}")