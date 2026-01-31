# 542. 01 Matrix
# BFS
# Distance of a neighbor = distance of current cell + 1
class Solution:
    def updateMatrix(self,a):
        q=[]
        v = [[False] * len(a[0]) for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j]==0:
                    q.append([i,j])
                    v[i][j]=True
        ans = [[0] * len(a[0]) for _ in range(len(a))]      
        l=0
        while q:
            x,y=q.pop(0)
            d=[[0,1],[1,0],[-1,0],[0,-1]]
            for k,z in d:
                    if 0<=k+x<len(a) and 0<=y+z<len(a[0]) and v[k+x][y+z]==False:
                            # check this out
                            ans[k+x][y+z]=ans[x][y]+1  
                            v[k+x][y+z]=True
                            q.append([k+x,y+z])
        return ans