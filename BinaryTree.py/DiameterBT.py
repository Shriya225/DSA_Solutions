# 543. Diameter of Binary Tree
def diameterOfBinaryTree(root):
    ans = 0

    def h(node):
        nonlocal ans
        if not node:
            return 0

        left = h(node.left)
        right = h(node.right)

        ans = max(ans, left + right)

        return 1 + max(left, right)

    h(root)
    return ans
