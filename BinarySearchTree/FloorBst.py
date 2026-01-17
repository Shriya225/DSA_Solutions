# gfg
# FLoor
class Solution:
    def floor(self, root, x):
        # code here
        ans=-1
        while root:
            if root.data==x:
                return x
            elif root.data<x:
                ans=root.data
                root=root.right
            else:
                root=root.left
        return ans