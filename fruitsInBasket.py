
def fruits(a):
        l=0
        ans=0
        d=dict()
        for r in range(len(a)):
            if not (a[r] in d):
                d[a[r]]=1
                print("d:",d)
                while len(d)>2:
                    d[a[l]]-=1
                    if d[a[l]]==0:
                        d.pop(a[l])
                    l+=1
            else:
                d[a[r]]+=1
                print("d",d)
            ans=max(ans,r-l+1)
        return ans
a=list(map(int,input("a:").split()))
print(fruits(a))