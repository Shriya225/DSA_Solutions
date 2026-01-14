# 101. Symmetric Tree
# dfs
def isSymmetric(self, root):
        def dfs(r1,r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            if r1.val!=r2.val:
                return False
            return dfs(r1.left,r2.right) and dfs(r2.left,r1.right)
        return dfs(root.left,root.right)