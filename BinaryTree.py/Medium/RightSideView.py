# naive bfs
# o(n) -sc ,tc

class Solution:
    def rightSideView(root):
        ans=[]
        if not root:
            return []
        q=[root]
        while q:
            n=len(q)
            l=[]
            for _ in range(n):
                x=q.pop(0)
                print(x)
                l.append(x.val)
                if x.right:
                    q.append(x.right)
                if x.left:
                    q.append(x.left)
            if l:
                ans.append(l[0])
        return ans
    


# optimal
# dfs
# rev of preorder (root right left)
def rightSideView(root):
        ans=[]
        def dfs(r,l=0):
            if not r:
                return
            # this is imp
            if len(ans)==l:
                ans.append(r.val)
            dfs(r.right,l+1)
            dfs(r.left,l+1)
        dfs(root)
        return ans