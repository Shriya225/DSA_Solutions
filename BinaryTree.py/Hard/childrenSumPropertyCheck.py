# check if 
# Children Sum in a Binary Tree is satified
# GFG Q.(Children Sum in a Binary Tree)

class Solution:
    def isSumProperty(self, root):
        # code here
            def dfs(r):
                if not r:
                    return -1
                x=dfs(r.left)
                # print("fs l ",x)
                if  x==False:
                    return False
                y=dfs(r.right)
                if  y==False:
                    return y
                if x==-1 and y==-1:
                    return r.data
                if (x==-1 and y!=r.data) or (y==-1 and x!=r.data):
                    return False
                if (x!=-1 and y!=-1) and x+y!=r.data:
                    return False
                return r.data
            return True if dfs(root) else False