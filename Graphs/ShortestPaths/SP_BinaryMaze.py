# 1091. Shortest Path in Binary Matrix
# A basic BFS in 8 dirs
# move only trough 0's
class Solution:
    def shortestPathBinaryMatrix(self, g):
        r,c=len(g),len(g[0])
        if g[0][0]==1 or g[r-1][c-1]==1:
            return -1
        if r-1==0 and c-1==0:
            return 1
        def bfs(g):
            v=[[False]*c for _ in range(r)]
            q=[[0,0]]
            v[0][0]=True
            ans=1
            while q:
                n=len(q)
                dir=[[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[1,1],[-1,1],[1,-1]]
                for _ in range(n):
                    x,y=q.pop(0)
                    for i,j in dir:
                        if 0<=x+i<r and 0<=y+j<c and not v[x+i][y+j] and g[x+i][y+j]==0:
                            q.append([x+i,y+j])
                            v[x+i][y+j]=True
                            if x+i==r-1 and y+j==c-1:
                                return ans+1
                ans+=1
            return -1
        return bfs(g)
        