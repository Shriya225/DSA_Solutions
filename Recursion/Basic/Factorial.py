
def factorial(n,f=1):
    if n==0:
        return f
    f*=n
    print(f,n)
    return factorial(n-1,f)

k=int(input("k:"))
print(factorial(k))