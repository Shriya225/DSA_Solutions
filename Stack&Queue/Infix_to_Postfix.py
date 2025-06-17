   
def Infix_to_Postfix(a):
    ans=''
    stk=[]
    priority={'+':1,'*':2,'/':2,'-':1,'^':3}
    for i in range(len(a)):
        if a[i] not in '+-*/^()':
            ans+=a[i]
        else:
            if not stk or a[i]=='(' or priority.get(stk[-1],-1)<priority.get(a[i],-1):
                stk.append(a[i])
            elif a[i]==')':
                while stk[-1]!="(":
                    ans+=stk.pop()
                stk.pop()
            elif priority.get(stk[-1],-1)>=priority.get(a[i],-1):
                while stk and priority.get(stk[-1],-1)>=priority.get(a[i],-1):
                    ans+=stk.pop()
                stk.append(a[i])
        print(stk,ans,a[i])
    while stk:
        ans+=stk.pop()
    return ans

a=input("a:")
print(Infix_to_Postfix(a))