# 1 - N
def OneToN(n,c=1):
    if c>n:
        return
    print(c)
    OneToN(n,c+1)

# N-1
def NToOne(n):
    if n==0:
        return
    print(n)
    NToOne(n-1)

k=int(input("k:"))
OneToN(k)
print('*'*10)
NToOne(k)