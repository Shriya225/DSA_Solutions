# 235. Lowest Common Ancestor of a Binary Search Tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# recursive
class Solution:
    def lowestCommonAncestor(self, root,p,q):
            if not root:
                return None
            
            if p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            
            if p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            
            return root
    
# iteratvie
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        x=root
        while x:
            if x.val<p.val and x.val<q.val:
                x=x.right
            elif x.val>p.val and x.val>q.val:
                x=x.left
            else:
                return root