# 56. Merge Intervals
class Solution:
    def merge(self, a):
        if not a:return []
        ans=[]
        a.sort(key=lambda x:x[0])
        prev=-2
        for ele in a:
            if ele[0]>prev:
                ans.append(ele)
                prev=ele[1]
            else:
                ans[-1][0]=min(ele[0],ans[-1][0])
                ans[-1][1]=max(ele[1],ans[-1][1])
                prev=ans[-1][1]
        return ans
    


# approach -2 
class Solution:
    def merge(self, a):
        if not a:return []
        ans=[]
        a.sort(key=lambda x:x[0])
        prev=-2
        for ele in a:
            if ele[0]>prev:
                ans.append(ele)
                prev=ele[1]
            else:
                x=ans.pop()
                ans.append([min(x[0],ele[0]),max(ele[1],x[1])])
                prev=max(ele[1],x[1])
        return ans
            