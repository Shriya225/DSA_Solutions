# Problem Statement: Given a Binary Tree, convert the value of its nodes to follow the Children Sum Property. The Children Sum Property in a binary tree states that for every node, the sum of its children's values (if they exist) should be equal to the node's value.
# If a child is missing, it is considered as having a value of 0.
def convertChildSUm(r):
    if not r:
        return
    if r.left and r.left.val<r.val:
        r.left.val=r.val
    if r.right and r.right.val<r.val:
        r.right.val=r.val
    convertChildSUm(r.left)
    convertChildSUm(r.right)
    x=0
    if r.right:
        x+=r.right.val
    if r.left:
        x+=r.left.val
    # for leaf nodes
    if r.let or r.right:
        r.val=x