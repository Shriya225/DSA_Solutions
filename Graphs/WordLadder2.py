# do bfs
# store paths while oding bfs only
# u will likely get TLE
class Solution:
    def findLadders(self, b: str,e: str, w):
        q=[[b]]
        c=[chr(ord('a')+i) for i in range(26)]
        if b in w:
            w.remove(b)
        ans=[]
        while q:
            n=len(q)
            r=[]
            for i in range(n):
                x=q.pop(0)
                y=x[-1]
                for j in range(len(y)):
                    for ch in c:
                        if y[:j]+ch+y[j+1:] in w:
                            np=x+[y[:j]+ch+y[j+1:]]
                            r.append(y[:j]+ch+y[j+1:])
                            q.append(np)
                            if y[:j]+ch+y[j+1:]==e:
                                ans.append(np)
            for k in r:
                if k in w:
                    w.remove(k)
            if ans:
                return ans
        return ans
            

