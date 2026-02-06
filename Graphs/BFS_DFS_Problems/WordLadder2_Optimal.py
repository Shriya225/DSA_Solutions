# do bfs - to find shortest paths
# store parents fr child nodes
# so tarverse back
# do dfs to backtarack to ifnd ans paths.
class Solution:
    def findLadders(self, b: str,e: str, w):
        q=[b]
        p=dict()
        c=[chr(ord('a')+i) for i in range(26)]
        if b in w:
            w.remove(b)
        ans=False
        while q:
            n=len(q)
            r=[]
            for i in range(n):
                y=q.pop(0)
                for j in range(len(y)):
                    for ch in c:
                        if y[:j]+ch+y[j+1:] in w:
                            np=y[:j]+ch+y[j+1:]
                            r.append(y[:j]+ch+y[j+1:])
                            if np in p:
                                p[np].append(y)
                            else:
                                p[np]=[y]
                            if np not in q:
                                q.append(np)
                            if y[:j]+ch+y[j+1:]==e:
                                ans=True
            for k in r:
                if k in w:
                    w.remove(k)
            if ans:
                break
        if not ans:return []
        ans=[]
        def dfs(e,s):
            if e==b:
                x=s[:]
                ans.append(x)
                return
            for i in p[e]:
                s.insert(0,i)
                dfs(i,s)
                s.pop(0)
        dfs(e,[e])
        return ans

            

