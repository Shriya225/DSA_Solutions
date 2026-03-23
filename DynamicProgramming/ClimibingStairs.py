# 70. Climbing Stairs

# WITHOUT DP (NORMAL RECURSION)

# For example, stairs(4) expands like this:

# stairs(4)
# ├── stairs(3)
# │   ├── stairs(2)
# │   │   ├── stairs(1)
# │   │   └── stairs(0)
# │   └── stairs(1)
# └── stairs(2)
#     ├── stairs(1)
#     └── stairs(0)


# Total calls ≈

# 1 + 2 + 4 + 8 + ... + 2^n

# This is a geometric series:

# ≈ 2^n
# tc- o(2^n)

c=0
def stairs(n):
    global c
    if n==0:
        c+=1
        return 1
    if n<0:
        return 0
    stairs(n-1)
    stairs(n-2)


# without using global variable
# cleaner code

def stairs(n):
    if n==0:
        return 1
    if n<0:
        return 0
    return stairs(n-1)+stairs(n-2)


# DP
# 1.memoization
def stairs(n):
    if n==0:
        return 1
    if n<0:
        return 0
    if dp[n]!=-1:
        return dp[n]
    dp[n]= stairs(n-1)+stairs(n-2)
    return dp[n]
n=int(input("n:"))
dp=[-1]*(n+1)


# tabualtion 
# same as fib no
# but dp[0]=1 will make it work
def stairs2(n):
    dp=[-1]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]



def stairs(n):
        if n == 0:
            return 1
        
        prev2 = 1   # dp[0]
        prev1 = 1   # dp[1]
        
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return prev1

n = int(input("n: "))
print(stairs(n))


