# 987. Vertical Order Traversal of a Binary Tree
def verticalTraversal(self, root):
        q=[[root,0,0]]
        d=dict()
        while q:
            node,hd,depth=q.pop(0)
            if hd not in d:
                d[hd]=[[node.val,depth]]
            else:
                d[hd].append([node.val,depth])
            if node.left:
                q.append([node.left,hd-1,depth+1])
            if node.right:
                q.append([node.right,hd+1,depth+1])
        y=sorted(d.keys())
        ans=[]
        for i in y:
            z=sorted(d[i],key=lambda x: (x[1], x[0]))
            l=[]
            for j in z:
                l.append(j[0])
            ans.append(l)
        return ans