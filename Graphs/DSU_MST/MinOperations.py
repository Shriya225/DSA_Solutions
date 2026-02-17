# 1319. Number of Operations to Make Network Connected
class Solution:
    def makeConnected(self, n: int,g) -> int:
        # A connected graph with n nodes needs at least n-1 edges
        if len(g) < n - 1:
            return -1
        parent = [i for i in range(n)]
        rank = [0] * n
        
        # Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # Union by rank
        def union(x, y):
            px = find(x)
            py = find(y)
            
            if px == py:
                return False  # cycle
            
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
            
            return True
        

        # 2.every time union succeeds , num of disonnected comonets decrease by 
        for x,y in g:
                union(x,y)
        # 1.count connected comonentss.
         
        ans=0
        for i in range(n):
            if find(i)==i:
                ans+=1
        return ans-1