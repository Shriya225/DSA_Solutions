# 1 2 2 3 4
# 2 3 3 4 5 6
def unionOfSorted(a,b):
    union=[]
    i=j=0
    while i<len(a) and j<len(b):
        while i<len(a)-1 and a[i]==a[i+1]:
            i+=1
        while j<len(b)-1 and b[j]==b[j+1]:
            j+=1
        if a[i]==b[j]:
            union.append(a[i])
            i+=1
            j+=1
        elif a[i]<b[j]:
            union.append(a[i])
            i+=1
        else:
            union.append(b[j])
            j+=1
    while i<len(a):
        while i<len(a)-1 and a[i]==a[i+1]:
            i+=1
        union.append(a[i])
        i+=1
    while j<len(b):
        while j<len(b)-1 and b[j]==b[j+1]:
            j+=1
        union.append(b[j])
        j+=1
    print("union:",union)
a=list(map(int,input("a:").split()))
b=list(map(int,input("a:").split()))
unionOfSorted(a,b)