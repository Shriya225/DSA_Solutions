# 1 2 3 4 5
# 5 4 3 2 1
# o(2n)==o(n)
def reverse(a):
    for i in range(len(a)//2):
        a[i],a[len(a)-1-i]=a[len(a)-1-i],a[i]
    print("rev",a)
def rotation(a,k):
    k=k%len(a)
    if k==0:
        print("a",a)
        return
    reverse(a)
    reverse(a[0:len(a)-k])
    reverse(a[len(a)-k:])
    print("a:",a)

x=[0,1,2,3]
print(x[:2])
l=list(map(int,input("a:").split()))
k=int(input("K:"))
rotation(l,k)
