# 1008. Construct Binary Search Tree from Preorder Traversal
# optimal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, p):
        i=0
        def dfs(l,r):
            nonlocal i
            if i==len(p):
                return None
            if p[i]<l or p[i]>r:
                return None
            x=TreeNode(p[i])
            i+=1
            x.left=dfs(l,x.val) 
            x.right=dfs(x.val,r)
            return x
        return dfs(float("-inf"),float("inf")) 