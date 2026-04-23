# 494. Target Sum

# reccurence rel'n

# this got submitted in Leetcode without TLE (lol...)
def ts(a, t, i):
    if i == 0:
        count = 0
        if t == a[0]:
            count += 1
        if t == -a[0]:
            count += 1
        return count

    l = ts(a, t - a[i], i - 1)  # take +
    r = ts(a, t + a[i], i - 1)  # take -
    return l + r

# memoization..
# using Dictionary,instead of steuggling eith size of dp..
class Solution:
    def findTargetSumWays(self, a, t):
        dp = {}

        def ts_memo(i, target):
            if i == 0:
                count = 0
                if target == a[0]:
                    count += 1
                if target == -a[0]:
                    count += 1
                return count

            if (i, target) in dp:
                return dp[(i, target)]

            l = ts_memo(i - 1, target - a[i])
            r = ts_memo(i - 1, target + a[i])

            dp[(i, target)] = l + r
            return dp[(i, target)]

        return ts_memo(len(a) - 1, t)
    
# tabualte
class Solution:
    def findTargetSumWays(self, a, target):
        dp = {0: 1}   # base case → 1 way to make sum 0

        for num in a:
            new_dp = {}
            for s in dp:
                # take +
                new_dp[s + num] = new_dp.get(s + num, 0) + dp[s]
                
                # take -
                new_dp[s - num] = new_dp.get(s - num, 0) + dp[s]
            
            dp = new_dp  # move to next index

        return dp.get(target, 0)


