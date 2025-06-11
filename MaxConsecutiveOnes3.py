
def maxOnes(a,k):
    x=k
    l=0
    ans=0
    for r in range(len(a)):
        if a[r]==0:
            x-=1
            if x<0:
                while x<0 and l<=r:
                    if a[l]==0:
                        x+=1
                    l+=1
                    print("ok b/w:",a[l:r+1],"here 0 are",x)
        print("ans:",r-l+1,a[l:r+1])
        ans=max(ans,r-l+1)
    return ans
            
            
a=list(map(int,input("a:").split()))
k=int(input("k:"))
print(maxOnes(a,k))