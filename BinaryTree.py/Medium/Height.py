#  DFS (Depth-First Search) on the binary tree.
#  Time & Space Complexity:
# Time Complexity: O(n) – every node is visited once.

# Auxiliary Space (recursive stack):

# In worst case (skewed tree): O(n)

# In best case (balanced tree): O(log n)
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


def maxDepth(root,c=0):
    if not root:
        return c
    left=maxDepth(root.left,c+1)
    right=maxDepth(root.right,c+1)
    return max(left,right)
print(maxDepth(root))

# max(left,right)+1
def maxDepth2(root):
    if not root:
        return 0
    return max(maxDepth2(root.left),maxDepth2(root.right))+1