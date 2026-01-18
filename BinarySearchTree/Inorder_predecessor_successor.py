# gfg
# both in 1 pass
class Solution:
    def findPreSuc(self, root, key):
        x=None
        y=None
        def dfs(r,k):
            nonlocal x,y
            while r:
                if r.data==k:
                    if r.left:
                        t=r.left
                        while t.right:
                            t=t.right
                        x=t
                    if r.right:
                        t=r.right
                        while t.left:
                            t=t.left
                        y=t
                    break
                elif r.data>k:
                    y=r
                    r=r.left
                else:
                    x=r
                    r=r.right
        dfs(root,key)
        return [x,y]