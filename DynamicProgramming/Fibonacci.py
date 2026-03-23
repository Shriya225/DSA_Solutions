# memoization(top-down)
# tc-O(n)
# sc-O(n)(arr to store values)+O(n)(stk space fr recursion)

# “Solve first, store later (on demand)”
def fib(n):
    if n<=1:
        return n
    if a[n]!=-1:
        return a[n]
    a[n]=fib(n-1)+fib(n-2)
    return a[n]
n=int(input("n:"))
a=[-1]*(n+1)
print(fib(n))

# tabulation(bottom-up)
# tc-o(n)
# sc-o(n)(arr to store)

# Tabulation literally means:

# “store solutions of all subproblems in a table (array)”

# “Store first, build upwards”
def fib2(n):
    dp=[-1]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]


# space optimized bottom -up approach

# Is space-optimized version “DP”?

# 👉 Yes, it is still Dynamic Programming

# Why?

# You’re still using the core DP idea:
# “build answer using previous results”
# You just don’t store all states, only what’s needed
def fib2(n):
    if n <= 1:
        return n

    prev2 = 0
    prev1 = 1

    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1

    
    