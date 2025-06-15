# fast and slow pointer logic
# 26. Remove Duplicates from Sorted Array
def reomveDuplicates(a):
    f=s=0
    while f<len(a):
        while f!=len(a)-1 and a[f]==a[f+1]:
            f+=1
        a[s]=a[f]
        s+=1
        f+=1
    print("arr is ,",a)

def remDups(a):
    s=0
    for i in range(len(a)):
        if i!=len(a)-1 and a[i]!=a[i+1]:
            a[s]=a[i]
            s+=1
    a[s]=a[-1]
    print("a",a)
l=list(map(int,input("a:").split()))
reomveDuplicates(l)