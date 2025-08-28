# def rev(a,l,h):
#     while l<=h:
#         a[l],a[h]=a[h],a[l]
#         l+=1
#         h-=1
# def rotateArr(a,k):
#     k=k%len(a)
#     rev(a,0,len(a)-1)
#     rev(a,0,k-1)
#     rev(a,k,len(a)-1)
#     print(a)

# def kadanes(a):
#     s=0
#     ans=float("-inf")
#     for i in a:
#         if s+i<0:
#             s=0
#         else:
#             s+=i
#         ans=max(ans,s)
        
# a=list(map(int,input("a:").split()))
# k=int(input("K:"))
# # rotateArr(a,k)

def lcp(a):
    x=a[0]
    for i in range(len(x)):
        for j in range(1,len(a)):
            if i>len(a[j]) or a[j][i]!=x[i]:
                return x[:i]
        return x
a=list(input("a:").split())