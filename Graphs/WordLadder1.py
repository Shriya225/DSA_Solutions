# bfs - optimal
class Solution:
    def ladderLength(self, b: str, e: str, w) -> int:
        if e not in w:
            return 0
        s=set(w)
        li=[chr(ord('a')+i) for i in range(26)]
        q=[b]
        if b in w:
            s.pop(b)
        ans=1
        while q:
            l=len(q)
            for i in range(l):
                x=q.pop(0)
                for k in range(len(x)):
                    for j in li:
                        if x[:k]+j+x[k+1:] in s:
                            q.append(x[:k]+j+x[k+1:])
                            s.remove(x[:k]+j+x[k+1:])
                            if x[:k]+j+x[k+1:]==e:
                                return ans+1
            ans+=1
        return 0



