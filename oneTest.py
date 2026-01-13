
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

root=Node(30)
root.left=Node(25)
root.right=Node(23)
root.left.left=Node(32)
root.left.right=Node(82)


def preOrder(root,ans=[]):
    ans=[]
    def dfs(root):
        if not root:
            return
        ans.append(root.val)
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return ans


def inorderTraversal(root):
        ans=[]
        stk=[]
        while root or stk:
            if not root and stk[-1][1]==0:
                ans.append(stk.pop()[0])
            elif not root and stk[-1][1]==1:
                root=stk.pop()[0]
            if root:
                if root.right:
                    stk.append([root.right,1])
                stk.append([root.val,0])
                root=root.left
        return ans



