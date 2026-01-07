
def outerParnts(s):
    stk=[]
    ans=""
    for i in s:
        if i=="(":
            if stk:
                ans+=i
            stk.append(i)
        elif i==")":
            if len(stk)>1:
                ans+=")"
            x=stk.pop()
    return ans



s=input("s:")
print(outerParnts(s))