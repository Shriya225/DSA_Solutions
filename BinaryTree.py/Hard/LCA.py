# 236. Lowest Common Ancestor of a Binary Tree

# ok find path to p,path to q and find lowest one there
# 2 tree traversal needed
class Solution:
    def findPath(self,root, target, path):
        if not root:
            return False
        path.append(root)
        if root == target:
            return True
        if self.findPath(root.left, target, path) or self.findPath(root.right, target, path):
            return True
        path.pop()
        return False

    def lowestCommonAncestor(self, root,p,q):
            path_p, path_q = [], []
            self.findPath(root, p, path_p)
            self.findPath(root, q, path_q)
            i = 0
            while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
                i += 1
            return path_p[i-1]