# 701. Insert into a Binary Search Tree

# recursive soln
# find search post and insert there
# blown mind away
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root,val):
        if not root:
            return TreeNode(val)
        if root.val>val:
            root.left=self.insertIntoBST(root.left,val)
        else:
            root.right=self.insertIntoBST(root.right,val)
        return root
    



# iteratvie one
class Solution:
    def insertIntoBST(self, root,val):
        if not root:
            return TreeNode(val)
        r2=root
        while root:
            if root.val>val:
                if not root.left:
                    root.left=TreeNode(val)
                    return r2
                root=root.left
                    
            else:
                if not root.right:
                    root.right=TreeNode(val)
                    return r2
                root=root.right