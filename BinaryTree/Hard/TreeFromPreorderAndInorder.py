# 105. Construct Binary Tree from Preorder and Inorder Traversal

# kinda brute (uses slicing)
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
    


# optimal
class Solution:
    def buildTree(self, p,i):
        d=dict()
        for k in range(len(i)):
            d[i[k]]=k
        pre_idx=0
        def helper(l,r):
            nonlocal pre_idx
            if l>r:
                return None
            x=d[p[pre_idx]]
            root=TreeNode(p[pre_idx])
            pre_idx+=1
            root.left=helper(l,x-1)
            root.right=helper(x+1,r)
            return root
        return helper(0,len(i)-1)