# 1020. Number of Enclaves
# do boundary dfs/bfs
class Solution:
    def numEnclaves(self, m ) -> int:
        def bfs(i,j):
            q=[[i,j]]
            while q:
                x,y=q.pop(0)
                dir=[[0,1],[1,0],[0,-1],[-1,0]]
                for k,z in dir:
                    if 0<=x+k<len(m) and 0<=y+z<len(m[0]) and m[x+k][y+z]==1:
                        m[x+k][y+z]="#"
                        q.append([x+k,y+z])
        for i in range(len(m)):
            if m[i][0]==1:
                m[i][0]="#"
                bfs(i,0)
            if m[i][len(m[0])-1]==1:
                m[i][len(m[0])-1]="#"
                bfs(i,len(m[0])-1)
        for i in range(len(m[0])):
            if m[0][i]==1:
                m[0][i]="#"
                bfs(0,i)
            if m[len(m)-1][i]==1:
                m[len(m)-1][i]="#"
                bfs(len(m)-1,i)
        # count ans
        ans=0
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j]=="#":
                    m[i][j]=1
                elif m[i][j]==1:
                    ans+=1
        return ans