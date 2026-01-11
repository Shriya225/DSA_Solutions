def infixToPostfix(a):
    stk=[]
    ans=''
    priority={"^":3,"/":2,"*":2,"+":1,"-":1}
    for i in range(len(a)):
        if a[i] not in "+-^*/()[]":
            ans+=a[i]
        elif a[i]==")":
            while stk[-1]!="(":
                ans+=stk.pop()
            stk.pop()
        else:
            while a[i]!="(" and stk and  priority[a[i]]<=priority[stk[-1]]:
                if a[i]=="^" and stk and priority[a[i]]==priority[stk[-1]]:
                    break
                ans+=stk.pop()           
            stk.append(a[i])
    while stk:
        ans+=stk.pop()
    return ans

s=input("s:")
print(infixToPostfix(s))




