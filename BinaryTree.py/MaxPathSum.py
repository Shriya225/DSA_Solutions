# 124. Binary Tree Maximum Path Sum
class Solution:
    def maxPathSum(root):
        ans = float("-inf")

        def h(node):
            nonlocal ans
            if not node:
                return 0

            # \very imp
            # wht if i want to discard subtree and go with onyform there,so ignore -ve subtreess
            left = max(0, h(node.left))  
            right = max(0, h(node.right))

            # path passing through this node
            ans = max(ans, left + right + node.val)

            # path extending upward
            return node.val + max(left, right)

        h(root)
        return ans
