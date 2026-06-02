# 1st June 2026

# 2144. Minimum Cost of Buying Candies With Discount
class Solution:
    def minimumCost(self, a):
        if len(a)<=2:
            return sum(a)
        a.sort()
        ans=0
        c=0
        for i in range(len(a)-1,-1,-1):
            if c==2:
                c=0
                continue
            if c<2:
                ans+=a[i]
                c+=1
        return ans


# cleaner code to skip evry 3rd ele from last
class Solution:
    def minimumCost(self, a):
        if len(a)<=2:
            return sum(a)
        a.sort()
        ans=0
        c=len(a)%3
        for i in range(len(a)-1,-1,-1):
            if i%3==c:
                continue
            ans+=a[i]
        return ans


# cleaner code 
# if we sort in reverse and try to fnd 3rd ele from 1st
class Solution:
    def minimumCost(self, cost):
        cost.sort(reverse=True)

        ans = 0
        for i in range(len(cost)):
            if i % 3 != 2:
                ans += cost[i]

        return ans