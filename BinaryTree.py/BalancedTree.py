


import math
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=TreeNode(1)
n2=TreeNode(2)
n3=TreeNode(3)
n4=TreeNode(4)
n5=TreeNode(5)
n6=TreeNode(6)
n7=TreeNode(7)
root.left=n2
root.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n2.right=n7

def isBalanced(root):
    if not root:
        return 0
    lh=isBalanced(root.left)
    rh=isBalanced(root.right)
    if lh==-1 or rh==-1:
        return -1
    if abs(lh-rh)>1:
        return -1
    return max(lh,rh)+1

def ans(root):
    return isBalanced(root)!=-1
print(ans(root))
    
    
    
