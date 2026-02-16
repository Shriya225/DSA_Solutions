# GFG
from typing import List

class Solution:
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: x[2])
        parent = [i for i in range(V)]
        rank = [0] * V
        
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
        ans=0
        e=0
        for x,y,z in edges:
            if union(x,y):
                ans+=z
                e+=1
            # optimization to stop after getting mst
            if e==V-1:
                break
        return ans


