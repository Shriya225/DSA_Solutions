# 662. Maximum Width of Binary Tree
class Solution:
    def widthOfBinaryTree(self, root):
        ans=float("-inf")
        def bfs(r):
            nonlocal ans
            q=[[r,1]]
            while q:
                n=len(q)
                l=[]
                for _ in range(n):
                    x=q.pop(0)
                    l.append(x[1])
                    if x[0].left:
                        q.append([x[0].left,x[1]*2])
                    if x[0].right:
                        q.append([x[0].right,(2*x[1])+1])
                if len(l)==1:
                    ans=max(ans,1)
                else:
                    ans=max(l[-1]-l[0]+1,ans)
        bfs(root)
        return ans