def nextpermutation(a):
    dip=-1
    for i in range(len(a)-1):
        if a[len(a)-i-2]<a[len(a)-i-1]:
            dip=len(a)-i-2
            break
    print(dip,a[dip])
    if dip!=-1:
        for i in range(len(a)):
            if a[len(a)-1-i]>a[dip]:
                a[dip],a[len(a)-1-i]=a[len(a)-1-i],a[dip]
                break
        print(a)
    a[dip+1:] = reversed(a[dip+1:])
    return a



a=list(map(int,input("a:").split()))
print(nextpermutation(a))