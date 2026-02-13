
class Solution:
    def findTheCity(self, n: int, edges, t: int) -> int:
        INF = 10**8
        g = [[INF]*n for _ in range(n)]
        for i in range(n):
            g[i][i] = 0
        for x,y,z in edges:
            g[x][y]=z
            g[y][x]=z
        n = len(g)
        INF = 10**8
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if g[i][k] != INF and g[k][j] != INF:
                        g[i][j] = min(g[i][j], g[i][k] + g[k][j])
        a=0
        m=float("inf")
        for i in range(n):
            c=0
            for k in g[i]:
                if k<=t:
                    c+=1
            if c<=m:
                m=c
                a=i
        return a
