# 3174. Clear Digits
def clearDigits( s: str) -> str:
        stk=[]
        for i in s:
            if i.isdigit() and stk:
                stk.pop()
            else:
                stk.append(i)
        return "".join(stk)
        