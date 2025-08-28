
def anagram(s,t):
        d=dict()
        for i in s:
            d[i]=d.get(i,0)+1
        for j in t:
            if j not in d:
                return False
            if j in d:
                d[j]-=1
                if d[j]==0:
                    d.pop(j)
        return True if not d else False
s=input("s:")
t=input("t:")