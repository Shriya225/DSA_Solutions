# 2385. Amount of Time for Binary Tree to Be Infected
class Solution:
    def amountOfTime(self, root,start):
        m=dict()
        tn=None
        m[root]=None
        def bfs(r):
            nonlocal tn
            q=[r]
            while q:
                x=q.pop(0)
                if x.val==start:
                    tn=x
                if x.left:
                    m[x.left]=x
                    q.append(x.left)
                if x.right:
                    m[x.right]=x
                    q.append(x.right)
        bfs(root)
        ans=0
        v=set()
        d=0
        v.add(tn)
        def bfs2(r):
            nonlocal ans,v,d
            q=[r]
            while q:
                n=len(q)
                for _ in range(n):
                    x=q.pop(0)
                    for ne in (x.left,x.right,m[x]):
                        if ne and ne not in v:
                            q.append(ne)
                            v.add(ne)
                d+=1
        bfs2(tn)
        return d-1
