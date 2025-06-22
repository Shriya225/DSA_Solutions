# 231. Power of Two
def isPowerof2(n,i=1):
    if i>n:
        return False
    if i==n:
        return True
    return isPowerof2(n,i*2)
n=int(input("n:"))
print(isPowerof2(n))