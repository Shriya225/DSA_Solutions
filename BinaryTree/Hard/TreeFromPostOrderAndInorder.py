# 106. Construct Binary Tree from Inorder and Postorder Traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        d=dict()
        for i in range(len(inorder)):
            d[inorder[i]]=i
        post_idx=len(postorder)-1
        def helper(l,r):
            nonlocal post_idx
            if l>r:
                return None
            idx=d[postorder[post_idx]]
            root=TreeNode(postorder[post_idx])
            post_idx-=1
            root.right=helper(idx+1,r)
            root.left=helper(l,idx-1)
            return root
        return helper(0,len(postorder)-1)