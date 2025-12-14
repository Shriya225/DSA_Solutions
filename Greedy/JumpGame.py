# 55. Jump Game
def jump(a):
    maxIndex=0
    for i in range(len(a)):
        if i>maxIndex:
            return False
        maxIndex=max(maxIndex,i+a[i])
    return True

a=list(map(int,input("c:").split()))
print(jump(a))