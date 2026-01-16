# 105. Construct Binary Tree from Preorder and Inorder Traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, p,i):
            ans=[]
            def buildT(p,i):
                if not p and not i:
                    return None
                z=i.index(p[0])
                root=TreeNode(p[0])
                root.left=buildT(p[1:1+z],i[:z])
                root.right=buildT(p[z+1:],i[z+1:])
                return root
            return buildT(p,i)