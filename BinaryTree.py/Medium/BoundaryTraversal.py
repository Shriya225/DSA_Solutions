# do it in gfg
# 3 dfs traversals
# o(n)
class Solution:
    def boundaryTraversal(self, root):
        # code here
        q=[]
        l=[root.data]
        leaf=[]
        r1=[]
        def dfs_l(r):
            if not r.left and not r.right:
               return
            l.append(r.data)
            if not r.left:
               dfs_l(r.right)
            else:
                dfs_l(r.left)
        if root.left:
            dfs_l(root.left)

        
        def dfs_leaves(r):
            if not r:
                return
            if not r.left and not r.right and (r!=root):
                leaf.append(r.data)
            dfs_leaves(r.left)
            dfs_leaves(r.right)
        dfs_leaves(root)

        
        def dfs_r(r):
            if not r or (not r.left and not r.right):
                return
            if r.right:
                dfs_r(r.right)
            else:
                dfs_r(r.left)
            r1.append(r.data)
        # start from right
        # if the root itelf has no riugth and u cant keep lookign for its left as it will go and become left boundary but not right
        if root.right:
            dfs_r(root.right)
        return l+leaf+r1