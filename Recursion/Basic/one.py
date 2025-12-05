# # print 1->N 
# def printNum(n):
#     if n<=0:
#         return
#     printNum(n-1)
#     print(n,end=" ")
# n=int(input("n:"))
# printNum(n)

# # factorial
# def fact(n):
#     if n<=0:
#         return 1
#     return n*fact(n-1)
# n=int(input("n:"))
# print(fact(n))

# # sum of n
# def sumOfNum(n):
#     if n<=0:
#         return 0
#     return (n%10)+sumOfNum(n//10)
# n=int(input("n:"))
# print(sumOfNum(n))

# rev arr inplace
# def revArr(a,n,i=0):
#     if i>(n//2):
#         return a
#     a[i],a[n-i-1]=a[n-i-1],a[i]
#     return revArr(a,n,i+1)


# a=list(map(int,input("a:").split()))
# print(revArr(a,len(a)))  

# def revArr2(a,l,h):
#     if l>h:
#         return a
#     a[l],a[h]=a[h],a[l]
#     return revArr2(a,l+1,h-1)
# a=list(map(int,input("a:").split()))
# print(revArr2(a,0,len(a)-1))  


# rev arr creat new arr
# def revArr3(a,n):
#     if n==0:
#         return [a[n]]
#     return [a[n]]+revArr3(a,n-1)
# a=list(map(int,input("a:").split()))
# print(revArr3(a,len(a)-1))  


# arr is sorted?
def SortedArr(a,n):
    if n==0:
        return True
    if a[n]<a[n-1]:
        return False
    return SortedArr(a,n-1)
a=list(map(int,input("a:").split()))
print(SortedArr(a,len(a)-1))