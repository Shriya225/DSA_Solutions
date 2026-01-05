# 205. Isomorphic Strings
# brute
def isIsomorphic(s: str, t: str) -> bool:
        d=dict()
        for i in range(len(s)):
            if s[i] in d and d[s[i]]!=t[i]:
                return False
            elif s[i] not in d:
                if t[i] in d.values():
                    return False
                d[s[i]]=t[i]
        return True