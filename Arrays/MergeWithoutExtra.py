# 4.	Merge two sorted arrays without using extra space.
# gap method..
import math
def nxtGap(n):
    if n<=1:
        return 0
    return math.ceil(n/2)
def merge(a,b):
    n,m=len(a),len(b)
    g=nxtGap(n+m)
    while g>0:
        i=0
        while i+g<n:
            if a[i]>a[i+g]:
                a[i],a[i+g]=a[i+g],a[i]
            i+=1
        j=0 if g<=n else g-n
        while i<n and j<m:
            if a[i]>b[j]:
                a[i],b[j]=b[j],a[i]
            i+=1
            j+=1
        if j<m:
            j=0
            while j+g<m:
                if b[j]>b[j+g]:
                    b[j],b[j+g]=b[j+g],b[j]
                j+=1
        g=nxtGap(g)
    print(a,b)

    
a=list(map(int,input("a:").split()))
b=list(map(int,input("b:").split()))
merge(a,b)