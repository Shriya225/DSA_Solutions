# 226. Invert Binary Tree

# dfs
def invertTree(self,root):
        def dfs(root):
            if not root:
                return 
            root.left,root.right=root.right,root.left
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return root

# BFS
def invertTree(self, root):
        q=[root]
        if not root:
            return root
        while q:
            x=q.pop(0)
            x.left,x.right=x.right,x.left
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        return root