
def PostfixToInfix(a):
    ans=''
    stk=[]
    for i in range(len(a)):
        if a[i] in "+-*^/":
            x=stk.pop()
            y=stk.pop()
            ans="("+y+a[i]+x+")"
            stk.append(ans)
        else:
            stk.append(a[i])
    return stk[-1]
a=input("a:")
print(PostfixToInfix(a))