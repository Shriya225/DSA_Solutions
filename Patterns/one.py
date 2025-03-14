def square(n):
    for i in range(n):
        print("*"*5)
    print()

def rectangle(l,b):
    for i in range(l):
        for j in range(b):
            print("*",end="")
        print()
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
        for j in range(i+1):
            print(j+1,end=" ")
        print()
    print()


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def pattern1(n):
    RightAngledTriangle(n)
    InvertedRightAngleTriangle(n-1)
    print()



#         * 
#       * *
#     * * *
#   * * * *
# * * * * *

def left_turned(n):
    # gaps observerd will always be l;ike 2*n-2 number
    # x=3 gaps =4
    # x=4 gaps =6
    gaps=2*n-2
    for i in range(n):
        print(" "*gaps,end="")
        gaps-=2
        for j in range(i+1):
            print("*",end=" ")
        print()
    print()



#      *
#     **
#    ***
#   ****
#  *****
# ******
def left_turned_no_gaps(n):
    # we can access rev from n-i-1
    for i in range(n):
        print(" "*(n-i-1),end="")
        print("*"*(i+1),end="\n")
    print()


# * * * * * * * * 
#   * * * * * * *
#     * * * * * *
#       * * * * *
#         * * * *
#           * * *
#             * *
#               *
def inverted_to_left(n):
    gaps=0
    for i in range(n):
        print(" "*gaps,end="")
        gaps+=2
        print("* "*(n-i))
    print()


# *******
#  ******
#   *****
#    ****
#     ***
#      **
#       *
def inverted_left_no_gaps(n):
    for i in range(n):
        print(" "*i,end="")
        print("*"*(n-i)) 
    print()  

#     *
#    ***
#   *****
#  *******
# *********
def pyramid_no_gap(n):
    for i in range(n):
        print(" "*(n-i-1),end="")
        print("*"*(2*i+1))
    print()

x=int(input("n:"))
square(x)
rectangle(int(input("enter l:")),int(input("enter b:")))
RightAngledTriangle(x)
print()
InvertedRightAngleTriangle(x)
NumberRAT(x)
pattern1(x)
left_turned(x)
left_turned_no_gaps(x)
inverted_to_left(x)
inverted_left_no_gaps(x)
pyramid_no_gap(x)




