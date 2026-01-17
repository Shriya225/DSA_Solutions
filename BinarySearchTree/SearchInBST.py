# 700. Search in a Binary Search Tree

# recursive
def searchBST(self, root,val):
    if not root:
        return None
    
    if root.val == val:
        return root
    
    if val < root.val:
        return self.searchBST(root.left, val)
    else:
        return self.searchBST(root.right, val)

# Iterative 
# clean
def searchBST2(self, root,val):
        ans=0
        while root:
            if root.val==val:
                return root
            elif root.val>val:
                root=root.left
            else:
                root=root.right
        return None
