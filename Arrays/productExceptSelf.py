# 238. Product of Array Except Self
# prefix&suffix Product
# without using // operator...
# o(n)-tc&sc
def productExceptSelf(a):
    n=len(a)
    prefixarr=[-1]*n
    suffixArr=[-1]*n
    ans=[-1]*n
    for i in range(n):
        if i==0:
            prefixarr[i]=a[i]
            suffixArr[-1]=a[n-1]
        else:
            prefixarr[i]=prefixarr[i-1]*a[i]
            suffixArr[n-i-1]=suffixArr[n-i]*a[n-i-1]
    print("pre",prefixarr,"suff",suffixArr)
    for i in range(n):
        if i==0:
            ans[i]=suffixArr[i+1]
            continue
        elif i==n-1:
            ans[i]=prefixarr[i-1]
            continue
        ans[i]=prefixarr[i-1]*suffixArr[i+1]
    print("ans:",ans)
l=list(map(int,input("A:").split()))
productExceptSelf(l)