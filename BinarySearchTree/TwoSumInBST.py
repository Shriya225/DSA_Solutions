# 653. Two Sum IV - Input is a BST
class Solution:
    def findTarget(self, root,k):
        ans=False
        s=set()
        def dfs(r,k):
            nonlocal ans
            if not r:
                return
            if k-r.val in s:
                ans=True
                return
            s.add(r.val)
            dfs(r.left,k)
            dfs(r.right,k)
        dfs(root,k)
        return ans