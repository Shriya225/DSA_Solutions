# 2696. Minimum String Length After Removing Substrings
def minLength( s: str) -> int:
        stk=[]
        for i in s:
            stk.append(i)
            if len(stk)>1 and (stk[-2]+stk[-1]=="AB" or stk[-2]+stk[-1]=="CD"):
                stk.pop()       
                stk.pop()
        return len(stk)  