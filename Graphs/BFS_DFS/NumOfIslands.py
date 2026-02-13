# 200. Number of Islands
# move 4 dirs
class Solution:
    def numIslands(self, g):
        ans=0
        r,c=len(g),len(g[0])
        def dfs(i,j):
            if g[i][j]=='0':
                return
            g[i][j]='0'
            if j!=0:
                dfs(i,j-1)
            if j!=c-1:
                dfs(i,j+1)
            if i!=0:
                dfs(i-1,j)
            if i!=r-1:
                dfs(i+1,j)
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j]=='1':
                    ans+=1
                    dfs(i,j)
        return ans