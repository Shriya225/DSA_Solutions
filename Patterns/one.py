def square(n):
    for i in range(n):
        print("*"*5)

def rectangle(l,b):
    for i in range(l):
        for j in range(b):
            print("*",end="")
        print()

def RightAngledTriangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()

def InvertedRightAngleTriangle(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        print()

def NumberRAT(n):
    for i in range(n):
        for j in range(n+1):
            print(j+1,end="")
        print()

x=int(input("Enter n:"))
square(x)
rectangle(int(input("enter l:")),int(input("enter b:")))
RightAngledTriangle(int(input("Enter n:")))
InvertedRightAngleTriangle(int(input("Enter n:")))