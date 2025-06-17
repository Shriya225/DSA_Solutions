# 150. Evaluate Reverse Polish Notation

# Revrese Polish notation is == postfix

# 10 6 9 3 + -11 * / * 17 + 5 +

def RPN(a):
    stk=[]
    for i in a:
        if i not in '+-*/':
            stk.append(int(i))
            print("i:",i,stk)
        else:
            x=stk.pop()
            y=stk.pop()
            ans=0
            if i=='+':
                ans=x+y
            elif i=='-':
                ans=y-x
            elif i=='*':
                ans=x*y
            else:
                ans=int(y/x)
            stk.append(ans)
            print(stk,"i:",i)
    return stk[0]
                
            


a=list(input("a:").split())
print(RPN(a))
print(int(6/132))