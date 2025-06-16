# 1876. Substrings of Size Three with Distinct Characters
def goodSubStr(a):
    d=dict()
    ans=0
    l=0
    for r in range(len(a)):
        if a[r] in d:
            d[a[r]]+=1
        else:
            d[a[r]]=1
        while d[a[r]]>1 or (r-l+1)>3:
            d[a[l]]-=1
            if d[a[l]]==0:
                d.pop(a[l])
            l+=1
        if (r-l+1)==3:
            ans+=1
    return ans

a=input("s:")
print(goodSubStr(a))