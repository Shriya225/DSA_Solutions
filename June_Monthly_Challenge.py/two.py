# 2nd June 2026

# 3633. Earliest Finish Time for Land and Water Rides I

# Brute Force O(m*n)
class Solution:
    # here only 2 rides t e done (1 from each)
    # try all possibilities of 2 combinations
    def earliestFinishTime(self,ls,ld,ws,wd):
        ans=float('inf')

        # go from left 1st then right 
        for i in range(len(ls)):
            x=ld[i]+ls[i]
            for j in range(len(ws)):
                if ws[j]<=x:
                    ans=min(ans,x+wd[j])
                else:
                    ans=min(ans,ws[j]+wd[j])
        # right 1s ttehn left
        for i in range(len(ws)):
            x=wd[i]+ws[i]
            for j in range(len(ls)):
                if ls[j]<=x:
                    ans=min(ans,x+ld[j])
                else:
                    ans=min(ans,ls[j]+ld[j])
        return ans


# bit more cleanre  code
class Solution:
    def earliestFinishTime(self, ls, ld, ws, wd):
        ans = float('inf')

        # Land -> Water
        for i in range(len(ls)):
            finish1 = ls[i] + ld[i]

            for j in range(len(ws)):
                finish2 = max(finish1, ws[j]) + wd[j]
                ans = min(ans, finish2)

        # Water -> Land
        for i in range(len(ws)):
            finish1 = ws[i] + wd[i]

            for j in range(len(ls)):
                finish2 = max(finish1, ls[j]) + ld[j]
                ans = min(ans, finish2)

        return ans
    

# Greedy
# O(m+n)
class Solution:
    def earliestFinishTime(self,ls,ld,ws,wd):
        ans=float('inf')
        x=float('inf')
        for i in range(len(ls)):
            x=min(x,ld[i]+ls[i])
        for j in range(len(ws)):
            ans=min(ans,max(x,ws[j])+wd[j])

        x=float('inf')
        for i in range(len(ws)):
            x=min(x,wd[i]+ws[i])
        for j in range(len(ls)):
            ans=min(ans,max(x,ls[j])+ld[j])
        return ans