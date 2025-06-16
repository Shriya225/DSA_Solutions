
# 424. Longest Repeating Character Replacement

def LCR(a,k):
    maxc=0
    d=dict()
    l=0
    ans=0
    for r in range(len(a)):
        if a[r] in d:
            d[a[r]]+=1
        else:
            d[a[r]]=1
        maxc=max(maxc,d[a[r]])
        # less freq ele is ntg but (len of window - max fre ele frequency)
        while (r-l+1)-maxc>k:
                d[a[l]]-=1
                if d[a[l]]==0:
                    d.pop(a[l])
                l+=1
        ans=max(ans,r-l+1)
    return ans

a=input("s:")
k=int(input("K:"))
print(LCR(a,k))