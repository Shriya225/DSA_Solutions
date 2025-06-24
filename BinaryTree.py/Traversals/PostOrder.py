# backtarcking style inorder traversal
# complex
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
n3.right=n7

def Postorder(root):
    if not root:
        return []
    stk = []
    ans = []
    while root or stk:
        while root:
            stk.append([root, 0]) 
            root = root.left
        while stk and stk[-1][1] == 1:
            node, _ = stk.pop()
            ans.append(node.data)
        if stk:
            stk[-1][1] = 1
            root = stk[-1][0].right
    return ans
print(Postorder(root))