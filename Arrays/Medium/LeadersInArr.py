def leaders(a):
    maxele=a[-1]
    ans=[a[-1]]
    for i in range(len(a)-2,-1,-1):
        if a[i]>maxele:
            ans.append(a[i])
            maxele=a[i]
    ans.reverse()
    return ans

a=list(map(int,input("a:").split()))
print(leaders(a))