class Solution:
    def floydWarshall(self, g):
        n = len(g)
    
        INF = 10**8
        # k = intermediate node
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if g[i][k] != INF and g[k][j] != INF:
                        g[i][j] = min(g[i][j], g[i][k] + g[k][j])
        
        return g