# def isPrime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# n=int(input("n:"))
# print(isPrime(n))

def sl(a):
    l=s=a[0]
    for i in range(len(a)):
        if a[i]>l:
            s=l
            l=a[i]
        if a[i]>s and a[i]<l:
            s=a[i]
    print(s,l)
a=list(map(int,input("a:").split()))
print(sl(a))