# gfg
# multisource dfs /bfs would do
# store shapes.
# how to?
# starting point is base
# subatrcting all connected points frm abse and store
# so we know simialr shapes and can avoid ocuntin them
#  This doesnot allwo roattion of islands **imp
class Solution:
    def countDistinctIslands(self, a ):
        v=[[False]*len(a[0]) for _ in range(len(a))]
        def dfs(i,j,bx,by,s):
            if not (0<=i<len(a) and 0<=j<len(a[0])) or a[i][j]==0 or v[i][j]:
                return
            v[i][j]=True
            s.append((bx-i,by-j))
            d=[[0,1],[0,-1],[1,0],[-1,0]]
            for x,y in d:
                dfs(i+x,j+y,bx,by,s)
    
        f=set()
        for i in range(len(a)):
            for j in range(len(a[0])):
                if not v[i][j] and a[i][j]==1:
                    s=[]
                    dfs(i,j,i,j,s)
                    f.add(tuple(sorted(s)))
        return len(f)

    