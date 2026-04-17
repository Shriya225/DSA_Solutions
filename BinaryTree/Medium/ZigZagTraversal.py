# 103. Binary Tree Zigzag Level Order Traversal
# bfs  + rev at each even level

# tc- o(n^2)
def zigzagLevelOrder(self, r):
        ans=[]
        q=[r]
        if not r:
            return []
        level=0
        while q:
            n=len(q)
            l=[]
            level+=1
            for _ in range(n):
                # this i o(n) ,so use deque
                x=q.pop(0)   
                l.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            if level%2==0:
                ans.append(l[::-1])
            else:
                ans.append(l)
        return ans

# bfs
# without reverse
def zigzagLevelOrder(r):
    if not r:
        return []

    ans = []
    q = [r]
    l_to_r = True

    while q:
        n = len(q)
        l = []

        for _ in range(n):
            x = q.pop(0)

            if l_to_r:
                l.append(x.val)
            else:
                # o(n) so use deque
                l.insert(0, x.val)

            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)

        ans.append(l)
        l_to_r = not l_to_r

    return ans
