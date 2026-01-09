# 503. Next Greater Element II
# monotnic stack approach
def nge2(a):
    n = len(a)
    ans = [-1] * n
    stk = []

    for i in range(2 * n):
        idx = i % n

        while stk and a[stk[-1]] < a[idx]:
            ans[stk.pop()] = a[idx]

        if i < n:          # 🔥 push only in first pass
            stk.append(idx)

    return ans

a=list(map(int,input("A:").split()))
print(nge2(a))