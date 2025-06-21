# print 1 k times using recursion

def printOne(k,c=0):
    if c==k:
        return
    printOne(k,c+1)
    print(1,"where c:",c)
k=int(input("k:"))
printOne(k)