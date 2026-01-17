# striver method
# keeep left /right as it is
# add right subtree to left max val
# retur root.left
class Solution:
    def deleteNode(self, root,key):
        if not root:
            return None
        if root.val>key:
            root.left=self.deleteNode(root.left,key)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            x=self.getRightMost(root.left)
            x.right=root.right
            return root.left
        return root
    def getRightMost(self, node):
        while node.right:
            node = node.right
        return node