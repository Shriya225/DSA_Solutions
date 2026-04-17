def levelOrder(self, root):
        q=[root]
        if not root:
            return []
        ans=[]
        while q:
            l=[]
            s=len(q)
            for _ in range(s):
                x=q.pop(0)
                l.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            if l:
                ans.append(l)
        return ans