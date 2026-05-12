# 673. Number of Longest Increasing Subsequence

# 673. Number of Longest Increasing Subsequence

def lis(a):
    n = len(a)

    dp = [1] * n      # LIS length
    ct = [1] * n      # number of LIS

    maxi = 1

    for i in range(n):

        for j in range(i):

            if a[j] < a[i]:

                # better LIS found
                if 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    ct[i] = ct[j]

                # same LIS length found
                elif 1 + dp[j] == dp[i]:
                    ct[i] += ct[j]

        maxi = max(maxi, dp[i])

    ans = 0

    for i in range(n):
        if dp[i] == maxi:
            ans += ct[i]

    return ans