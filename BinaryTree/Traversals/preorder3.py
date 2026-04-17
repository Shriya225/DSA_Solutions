# a variant of inorder
def preorder(root):
    if not root:
        return []
    stk = [root]
    ans = []
    while stk:
        node = stk.pop()
        ans.append(node.data)
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)
    return ans