
def topView(self, root):
        # code here
        if not root:
            return []
        q=[[root,0]]
        d=dict()
        while q:
                x=q.pop(0)
                d[x[1]]=x[0].data
                if x[0].left:
                        q.append([x[0].left,x[1]-1])
                if x[0].right:
                        q.append([x[0].right,x[1]+1])
        ans=[]
        y=sorted(d.keys())
        for i in y:
            ans.append(d[i])
        return ans