# 50. Pow(x, n)
# iterative o(n)
# def pow(x,n):
#     ans=1
#     for _ in range(n):
#         ans*=x
#     return ans

# recursive tc-o(n) sc-o(n)
# def pow(x,n,ans=1):
#     if n==0:
#         return ans
#     return pow(x,n-1,ans*x)


def pow(x,n):
    if n==0:
        return 1
    half=pow(x,n//2)
    if n%2==0:
        return half*half
    else:
        return x*half*half


x=int(input("x:"))
n=int(input("n:"))
print(pow(x,n))