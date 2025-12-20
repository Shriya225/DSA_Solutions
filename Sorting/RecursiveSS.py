
def rss(a,i,n):
    if n==0 or n==1:
        return a
    if i==n-1:
        return a
    minele=i
    for j in range(i,n):
        if a[j]<a[minele]:
            minele=j
    a[i],a[minele]=a[minele],a[i]
    return rss(a,i+1,n)


a=list(map(int,input("a:").split()))
print(rss(a,0,len(a)))