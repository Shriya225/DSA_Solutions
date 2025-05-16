def productExceptSelf(a):
    totalProduct=1
    ans=[-1]*len(a)
    for i in range(len(a)):
        totalProduct*=a[i]
    for i in range(len(a)):
        if i==0 and a[i]!=0:
            ans[i]=totalProduct//a[i]
            continue
        if a[i]!=0:
            ans[i]=totalProduct//(a[i])
    print(ans)
l=list(map(int,input("A:").split()))
productExceptSelf(l)