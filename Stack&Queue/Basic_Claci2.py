# 227. Basic Calculator II
# conveting it to postfix & the evaluatin g it ....
def conversion(s):
    stk=[]
    ans=[]
    i=0
    precedence={'^':3,'+':1,'-':1,'*':2,'/':2}
    while i<len(s):
        if s[i]==' ':
            i+=1
            continue
        if s[i].isdigit():
            x=s[i]
            while i+1<len(s) and s[i+1].isdigit():
                x+=s[i+1]
                i+=1
            ans.append(x)
        elif not stk:
            stk.append(s[i])
        elif precedence[stk[-1]]>=precedence[s[i]]:
            while stk and precedence[stk[-1]]>=precedence[s[i]]:
                ans.append(stk.pop())
            stk.append(s[i])
        else:
            stk.append(s[i])
        i+=1
    while stk:
        ans.append(stk.pop())   
    print(ans)
    return ans

def basic_Calci2(s):
    converted_exp=conversion(s)
    stk=[]
    for i in converted_exp:
        if i not in '+-*/':
            stk.append(int(i))
        elif len(stk)>1:
            x=int(stk.pop())
            y=int(stk.pop())
            if i=='+':
                stk.append(x+y)
            elif i=="-":
                stk.append(y-x)
            elif i=='*':
                stk.append(y*x)
            else:
                stk.append(int(y/x))
    return stk[0]


s=input("s:")
print(conversion(s))
print(basic_Calci2(s))