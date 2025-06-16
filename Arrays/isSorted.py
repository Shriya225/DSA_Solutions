def isSorted(a):
    for i in range(len(a)):
        asc=True
        if i!=len(a)-1 and a[i]>a[i+1]:
            asc=False
            break
    print("asc",asc)
    for i in range(len(a)):
        desc=True
        if i!=len(a)-1 and a[i]<a[i+1]:
            desc=False
            break
    print("desc",desc)
    
        


l=list(map(int,input("a:").split()))
isSorted(l)
