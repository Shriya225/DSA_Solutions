# 1614. Maximum Nesting Depth of the Parentheses
def maxDepth( s: str) -> int:
        stk=[]
        c=0
        ans=0
        for i in s:
            if i=="(":
                stk.append(i)
                c+=1
                ans=max(ans,c)
            elif i==")":
                stk.pop()
                c-=1
        return ans