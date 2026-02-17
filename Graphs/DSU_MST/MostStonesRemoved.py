# 947. Most Stones Removed with Same Row or Column
class Solution:
    def removeStones(self, g) -> int:
        n=len(g)
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
        # connect eles based on inde of stones array
        # O(n²) pair comparison
        # stone-to-stone connections…
        for i in range(n):
            for j in range(i+1,n):
                if g[i][0]==g[j][0] or g[i][1]==g[j][1]:
                    union(i,j)
        ans=0
        for i in range(n):
            if find(i)==i:
                ans+=1
        return n-ans
    

# before : stoen<==>stone
# now : row <==> col  (here stoen beomces edges) 

# If two stones share:
# Same row
# They connect to same row node.
# Same column
# They connect to same column node.
# So through row/column nodes, they become connected.
# No need to compare every pair.


# 947. Most Stones Removed with Same Row or Column

# cannot use parent array as col|+offset is big arr can become large,better use dict
class Solution:
    def removeStones(self, stones):
        parent = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parent[px] = py
        
        for r, c in stones:
            union(r, c + 10001)   # offset columns
        
        roots = set()
        for r, c in stones:
            roots.add(find(r))
        
        return len(stones) - len(roots)
    


        