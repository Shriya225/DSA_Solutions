# 860. Lemonade Change
def change(b):
    d={5:0,10:0}
    for i in b:
        if i==5:
            d[5]+=1
        elif i==10:
            if d[5]>0:
                d[5]-=1
                d[10]+=1
            else:
                return False
        elif i==20:
            if d[10]>0 and d[5]>0:
                d[10]-=1
                d[5]-=1
            elif d[5]>=3:
                d[5]-=3
            else:
                return False
    return True



c=list(map(int,input("c:").split()))
print(change(c))