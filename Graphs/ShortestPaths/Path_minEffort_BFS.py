# BFS+ Binary Search
class Solution:
    def minimumEffortPath(self, g):
        e=0
        m=float('inf')
        for i in g:
            for j in i:
                m=min(j,m)
                e=max(j,e)
        h=e-m
        def helper(k):
            v=[[False]*len(g[0]) for i in range(len(g))]
            q=[(0,0)]
            v[0][0]=True
            while q:
                i,j=q.pop(0)
                d=[[0,1],[1,0],[-1,0],[0,-1]]
                for x,y in d:
                    if 0<=i+x<len(g) and 0<=j+y<len(g[0]) and not v[i+x][j+y]:
                        if abs(g[i+x][j+y]-g[i][j])<=k:
                            v[i+x][j+y]=True
                            if i+x==len(g)-1 and j+y==len(g[0])-1:
                                return True
                            q.append([i+x,j+y])
            return False
        def bs(g,h):
            l=0
            ans=0
            while l<=h:
                m=(l+h)//2
                if helper(m):
                    ans=m
                    h=m-1
                else:
                    l=m+1
            return ans
        x=bs(g,h)
        return x

                