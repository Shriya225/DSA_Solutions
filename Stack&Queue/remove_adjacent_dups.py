# 1047. Remove All Adjacent Duplicates In String
# A classic UseCase of Stack!!!

def removeDuplicates(self, s: str) -> str:
        stk=[]
        for i in s:
            if not stk:
                stk.append(i)
            elif  stk[-1]==i:
                stk.pop()
            else:
                stk.append(i)
        return "".join(stk)
        