# brute force o(n) space
# just store preorder and 
# change tree
class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        ans=[]
        def dfs(r):
            if not r:
                return
            ans.append(r)
            dfs(r.left)
            dfs(r.right)
        dfs(root)

        x=len(ans)
        i=0
        for i in range(len(ans) - 1):
            ans[i].left = None
            ans[i].right = ans[i + 1]

        if ans:
            ans[-1].left = None
            ans[-1].right = None
        return root