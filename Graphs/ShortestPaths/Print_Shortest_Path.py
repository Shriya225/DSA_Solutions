# given 1 src and 1 dest
# print shortest apth b/w it
# do dijkstar + parent map storage
import heapq
def print_sp(g,s,d):
    def dij(g,s,d):
        ans=[float('inf')]*len(g)
        parent=[-1]*len(g)
        ans[s]=0
        pq=[]
        heapq.heappush(pq,(0,s))
        while pq:
            dist,p=heapq.heappop(pq)
            if dist>ans[p]:
                continue
            if p==d:
                return parent
            for n,wt in g[p]:
                if dist+wt<ans[n]:
                    ans[n]=dist+wt
                    parent[n]=p
                    heapq.heappush(pq,(dist+wt,n))
        return parent
    p=dij(g,s,d)
    x=d
    ans=[d]
    while x!=s:
        if p[x]==-1:
            return [-1]
        ans.append(p[x])
        x=p[x]
    return ans[::-1]



                
