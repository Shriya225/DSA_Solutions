# BackTracking

def rootToNode(root, x):
    stk = []
    ans = []

    def dfs(r):
        if not r:
            return False

        stk.append(r.val)

        if r.val == x:
            ans[:] = stk[:]  # Copy current path to ans
            return True

        if dfs(r.left) or dfs(r.right):
            return True

        stk.pop()  # Backtrack
        return False

    dfs(root)
    return ans

        
