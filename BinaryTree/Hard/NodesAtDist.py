# 863. All Nodes Distance K in Binary Tree
class Solution:
    def distanceK(self, root,t,k) :
        m = dict()
        m[root] = None
        
        def dfs(r):
            if not r:
                return
            if r.left:
                m[r.left] = r
            if r.right:
                m[r.right] = r
            dfs(r.left)
            dfs(r.right)
        dfs(root)
        
        d = 0
        ans = []
        v = set()
        q = [t]
        v.add(t)  # Mark target as visited BEFORE BFS starts
        
        def bfs():
            nonlocal d, ans
            while q:
                n = len(q)
                if d == k:
                    for node in q:
                        ans.append(node.val)
                    return
                for _ in range(n):
                    x = q.pop(0)
                    # Already visited on enqueue, so no need to add here
                    
                    for nei in (x.left, x.right, m[x]):
                        if nei and nei not in v:
                            q.append(nei)
                            v.add(nei)
                d += 1
                
        bfs()
        return ans
