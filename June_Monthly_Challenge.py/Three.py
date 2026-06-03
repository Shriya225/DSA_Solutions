# June 3 , 2026
# 3635. Earliest Finish Time for Land and Water Rides II

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
    
# same as 2nd june ques ,but constraits are different,so brute fails here and ony greedy works.
# better aporach is sorting+bserach O(nlogm)
# bt opitmal is this greedy O(n+m)