# ss not stable
# ss not adaptive
def ss(a):
    n=len(a)
    for i in range(n):
        minele=i
        for j in range(i,n):
            if a[minele]>a[j]:
                minele=j
        a[i],a[minele]=a[minele],a[i]
    return a
a=list(map(int,input("a:").split()))
print(ss(a))