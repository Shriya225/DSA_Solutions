# 402. Remove K Digits
def removeDigits(a,k):
    stk=[]
    for i in a:
        while stk and k>0 and stk[-1]>i:
            stk.pop()
            k-=1
        stk.append(i)
    while k!=0:
        stk.pop()
        k-=1
    x= "".join(stk).lstrip("0") 
    return x if x else "0"
    
s=input("s:")
k=int(input("k:"))
print(removeDigits(s,k))