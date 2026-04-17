# basic dfs
# naive soln
class Solution:
    def countNodes(self, root):
        ans=0
        def dfs(r):
            nonlocal ans
            if not r:
                return
            ans+=1
            dfs(r.left)
            dfs(r.right)
        dfs(root)
        return ans


# clean and without nonlocal

# works fr any BT
# O(log N) * O(log N) = O(log² N)

def countNodes(self, root):
    def dfs(r):
        if not r:
            return 0
        x = dfs(r.left)
        y = dfs(r.right)
        return x + y + 1
    return dfs(root)



# optimal soln

# works only fr ** complete BT **

class Solution:
    def countNodes(self, root):

        def lhf(r):
            h=0
            while r:
                h+=1
                r=r.left
            return h

        def rhf(r):
            h=0
            while r:
                h+=1
                r=r.right
            return h

        lh=lhf(root)
        rh=rhf(root)
        if lh==rh:
            return (2**lh)-1
        return 1+(self.countNodes(root.left)+self.countNodes(root.right))