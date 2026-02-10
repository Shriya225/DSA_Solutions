# using dij
import heapq
class Solution:
    def shortestPathBinaryMatrix(self, g):
        r,c=len(g),len(g[0])
        if g[0][0]==1 or g[r-1][c-1]==1:
            return -1
        if r-1==0 and c-1==0:
            return 1
        def dij(g):
            pq=[]
            heapq.heappush(pq,(1,(0,0)))
            ans=[[float('inf')]*c for i in range(r) ]
            ans[0][0]=1
            while pq:
                k,t=heapq.heappop(pq)
                x,y=t
                if x==r-1 and y==c-1:
                    return ans[-1][-1]
                if ans[x][y]<k:
                    continue
                dir=[[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[1,1],[-1,1],[1,-1]]
                for i,j in dir:
                        if 0<=x+i<r and 0<=y+j<c  and g[x+i][y+j]==0:
                            if k+1 < ans[x+i][y+j]:
                                ans[x+i][y+j]=k+1
                                heapq.heappush(pq,(k+1,(x+i,y+j)))
            return ans[-1][-1] if ans[-1][-1]!=float("inf") else -1
        return dij(g)