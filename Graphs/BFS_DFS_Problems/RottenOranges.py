# Do multi source BFS
# 994. Rotting Oranges
class Solution:
    def orangesRotting(self, g) -> int:
            q=[]
            c=0
            for i in range(len(g)):
                for j in range(len(g[0])):
                    if g[i][j]==2:
                        q.append([i,j])
                    elif g[i][j]==1:
                        c+=1
            ans=0
            while q:
                n=len(q)
                f=False
                for i in range(n):
                    x,y=q.pop(0)
                    if x+1<len(g) and g[x+1][y]==1:
                        q.append([x+1,y])
                        g[x+1][y]=2
                        c-=1
                    if y+1<len(g[0]) and g[x][y+1]==1:
                        c-=1
                        q.append([x,y+1])
                        g[x][y+1]=2
                    if x-1>-1 and g[x-1][y]==1:
                        c-=1
                        g[x-1][y]=2
                        q.append([x-1,y])
                    if y-1>-1 and g[x][y-1]==1:
                        c-=1
                        g[x][y-1]=2
                        q.append([x,y-1])
                    
                    ans+=1
                if c==0:
                    return ans
            return -1
    
# cleaner soln
from collections import deque
class Solution:
    def orangesRotting(self, g) -> int:
            q=deque()
            c=0
            for i in range(len(g)):
                for j in range(len(g[0])):
                    if g[i][j]==2:
                        q.append([i,j])
                    elif g[i][j]==1:
                        c+=1
            ans=0
            while q and c!=0:
                n=len(q)
                for i in range(n):
                    x,y=q.popleft()
                    dir=[[0,1],[0,-1],[-1,0],[1,0]]
                    for k,z in dir:
                        if 0<=x+k<len(g) and 0<=y+z<len(g[0]) and g[x+k][y+z]==1:
                            g[x+k][y+z]=2
                            q.append([x+k,y+z])
                            c-=1
                ans+=1
            return ans if c==0 else -1

