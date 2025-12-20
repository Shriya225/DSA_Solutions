# my version of swapping to insert.
def Is(a):
    n=len(a)
    for i in range(1,n):
        if a[i]<a[i-1]:
            j=i
            while j>0 and a[j]<a[j-1]:
                a[j],a[j-1]=a[j-1],a[j]
                j-=1
    return a
a=list(map(int,input("a:").split()))
print(Is(a))

# textbook version of shifting to insert.
def Is(a):
    n=len(a)
    for i in range(1,n):
        if a[i]<a[i-1]:
            key=a[i]
            j=i-1
            while j>0 and a[j]>key:
                a[j+1]=a[j]
                j-=1
            a[j+1]=key
    return a
a=list(map(int,input("a:").split()))
print(Is(a))