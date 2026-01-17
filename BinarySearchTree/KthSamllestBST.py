# inorder tarversal
# recurisve
# 230. Kth Smallest Element in a BST
class Solution:
    def kthSmallest(self, root,k):
        x=0
        ans=0
        def dfs(r):
            nonlocal x,ans
            if not r:
                return False
            dfs(r.left)
            x+=1
            if x==k:
                ans=r.val
                return True
            dfs(r.right)
        dfs(root)
        return ans