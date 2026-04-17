# 297. Serialize and Deserialize Binary Tree

# just do dfs by adding null values too

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s=''
        def dfs(r):
            nonlocal s
            if not r:
                s+='x,'
                return
            s+=str(r.val)+","
            dfs(r.left)
            dfs(r.right)
        dfs(root)
        return s
            

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        s=data.split(',')
        i=0
        def helper():
            nonlocal i
            if s[i]=='x':
                i+=1
                return None
            r=TreeNode(int(s[i]))
            i+=1
            r.left=helper()
            r.right=helper()
            return r
        return helper()