# 1869. Longer Contiguous Segments of Ones than Zeros
def checkZeroOnes(a):
    ones=zeros=maxone=maxzero=0
    for i in range(len(a)):
        if a[i]=='1':
            zeros=0
            ones+=1
            maxone=max(maxone,ones)
        else:
            ones=0
            zeros+=1
            maxzero=max(maxzero,zeros)
        # print("maxone",maxone,"maxzero",maxzero)
    if maxone>maxzero:
        return True
    return False
s=input("s:")
print(checkZeroOnes(s))