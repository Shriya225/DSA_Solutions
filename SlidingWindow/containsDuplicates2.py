# 219. Contains Duplicate II
# using Dictionary
# TC-O(n)
# SC-O(n)
def dups(a,k):
        if len(a)==1:
            return False
        d=dict()
        for i in range(len(a)):
                if a[i] in d and i-d[a[i]]<=k:
                    return True
                d[a[i]]=i
        return False

a=list(map(int,input("a:").split()))
k=int(input("k:"))
print(dups(a,k))
