# Time Complexity = O(2ⁿ)
# 🧠 Rule of thumb:
# Whenever a recursive function calls itself more than once, and the subproblems overlap, 
# the number of calls can grow exponentially unless we use memoization.

# So What’s the Maximum Depth?
# The deepest path in this recursion is fib(n) → fib(n-1) → fib(n-2) → ... → fib(1),
#  so the maximum depth of the call stack is:
# 🔹 O(n) (because we go all the way down from n to 1 in the worst path)

def nthFibonacci(n):
    if n==0 or n==1:
        return n
    return nthFibonacci(n-2)+nthFibonacci(n-1)
    