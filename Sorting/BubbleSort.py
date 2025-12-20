# bs is stable algo.
def bs(a):
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
a=list(map(int,input("a:").split()))
print(bs(a))



# Adaptive bubble sort.
def bs2(a):
    n=len(a)
    for i in range(n):
        swapped=False
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swapped=True
        if not swapped:
            break
    return a
a=list(map(int,input("a:").split()))
print(bs2(a))


# bs desc order.
def bs2(a):
    n=len(a)
    for i in range(n):
        swapped=False
        for j in range(n-i-1):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swapped=True
        if not swapped:
            break
    return a
a=list(map(int,input("a:").split()))
print(bs2(a))