# my version
def postorderTraversal(self, root) :
        stk=[]
        ans=[]
        if not root:
            return []
        while root or stk:
            if not root:
                if stk[-1][1]==0:
                    ans.append(stk[-1][0])
                else:
                    root=stk[-1][0]
                stk.pop()
            if root:
                stk.append([root.val,0])
                if  root.right:
                    stk.append([root.right,1])
                root=root.left
        return ans

# 2stks
def postorderTraversal2(self, root) :
        stk=[root]
        ans=[]
        if not root:
            return []
        while stk:
            x=stk.pop()
            ans.append(x.val)
            if x.left:
                stk.append(x.left)
            if x.right:
                stk.append(x.right)
        return ans[::-1]

# 1stk

def postorderTraversal(self, root):
    ans = []
    stack = []
    curr = root
    lastVisited = None

    while curr or stack:
        # Go as left as possible
        while curr:
            stack.append(curr)
            curr = curr.left

        node = stack[-1]

        # If right child exists AND not yet processed → go right
        if node.right and lastVisited != node.right:
            curr = node.right
        else:
            # Both children done → process node
            ans.append(node.val)
            lastVisited = stack.pop()

    return ans
