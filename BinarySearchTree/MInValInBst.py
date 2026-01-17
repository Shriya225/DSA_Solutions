# min value is left most
# max value is right most
def minValue(self, root):
        # code here
        if not root:
            return None
        ans=0
        while root:
            ans=root.data
            root=root.left
        return ans