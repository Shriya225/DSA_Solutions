
def convert_to_Prefix(a):
    stk=[]
    ans=''
    precedence={'^':3,'+':1,'-':1,'*':2,'/':2}
    for i in range(len(a)-1,-1,-1):
        if a[i] not in '+-/*^()':
            ans=a[i]+ans
        else:
            if a[i]==")":
                stk.append(a[i])
            elif a[i]=="(":
                while stk and stk[-1]!=')':
                    ans=stk.pop()+ans
                stk.pop()
            elif not stk:
                stk.append(a[i])
            elif precedence.get(stk[-1],-1)>precedence.get(a[i],-1) or (precedence.get(stk[-1],-1)==precedence.get(a[i],-1) and (a[i]=="^" )) :
                while stk and (precedence.get(stk[-1],-1)>precedence.get(a[i],-1) or (precedence.get(stk[-1],-1)==precedence.get(a[i],-1) and (a[i]=="^" ))):
                    ans=stk.pop()+ans

                stk.append(a[i])
            else:
                stk.append(a[i])
        print(stk,ans,"iad: ",a[i])
    while stk:
        ans=stk.pop()+ans
    return ans
            
a=input("a:")
print(convert_to_Prefix(a))