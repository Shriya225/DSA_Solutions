# 98. Validate Binary Search Tree
# preorder wit range check fr evry node
class Solution:
    def isValidBST(self, root):
        
        def dfs(r,l,h):
            if not r:
                return True
            if r.val<=l or r.val>=h:
                return False
            if not dfs(r.left,l,r.val):
                return False
            if not dfs(r.right,r.val,h):
                return False
            return True
        return dfs(root,float("-inf"),float("inf"))