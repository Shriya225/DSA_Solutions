def reverseArray(a):
    n=len(a)
    for i in range(len(a)//2):
        a[i],a[n-i-1]=a[n-i-1],a[i]
    return a