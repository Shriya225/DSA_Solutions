# 3090. Maximum Length Substring With Two Occurrences

def maxlen(a):
        d=dict()
        l=0
        ans=0
        for r in range(len(a)):
            if a[r] in d:
                d[a[r]]+=1
            else:
                d[a[r]]=1
            while d[a[r]]>2:
                d[a[l]]-=1
                if d[a[l]]==0:
                    d.pop(a[l])
                l+=1
            ans=max(ans,r-l+1)
        return ans
        
a=input("a:")
print(maxlen(a))