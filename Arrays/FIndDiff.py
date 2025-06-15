# 389. Find the Difference
def findTheDifference(s: str, t: str) -> str:
        d={}
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1
        for j in range(len(t)):
            if t[j] not in d or d[t[j]]==0:
                return t[j]
            d[t[j]]-=1