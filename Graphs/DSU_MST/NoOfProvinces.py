class Solution:
    def findCircleNum(self, g) -> int:
        parent = [i for i in range(len(g))]
        rank = [0] * len(g)
        
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
        

        # 2.every time union succeeds , num of disonnected comonets decrease by 1.
        ans=len(g)
        for i in range(len(g)):
            for j in range(len(g[0])):
                if i!=j and g[i][j]==1:
                    if union(i,j):
                        ans-=1
        return ans
    


# ...........................

# 1.count connected comonentss.
class Solution:
    def findCircleNum(self, g) -> int:
        parent = [i for i in range(len(g))]
        rank = [0] * len(g)
        
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
        

        # 2.every time union succeeds , num of disonnected comonets decrease by 1.
        for i in range(len(g)):
            for j in range(len(g[0])):
                if i!=j and g[i][j]==1:
                    union(i,j)
        # 1.count connected comonentss.
         
        ans=0
        for i in range(len(g)):
            if find(i)==i:
                ans+=1
        return ans
    

        



    

        


