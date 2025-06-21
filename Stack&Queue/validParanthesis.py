# 20. Valid Parentheses
def isValid(s):
        stk=[]
        d={')':"(","]":"[","}":"{"}
        for i in s:
            if i in '({[':
                stk.append(i)
            elif stk and d[i]==stk[-1]:
                stk.pop()
            else:
                return False
        return True if not stk else False
s=input("s:")
print(isValid(s))