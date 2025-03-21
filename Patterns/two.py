# *********
#  *******
#   *****
#    ***
#     *

def inverted_pyramid(n):
    # it has odd number of satrs
    # (2n+1) gives oddn numbers from (0,1,2,..)
    for i in range(n):
        print(" "*i,end="")
        print("*"*(2*(n-i-1)+1))


#     * 
#    * *
#   * * *
#  * * * *
# * * * * *

def triangle_start_pattern(n):
    for i in range(n):
        print(" "*(n-i-1),end="")
        print("* "*(i+1))



# * * * * *
#  * * * *
#   * * *
#    * *
#     *

def inverted_traingle_pattern(n):
    for i in range(n):
        print(" "*i,end="")
        print("* "*(n-i))


# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
def hour_glass(n):
    inverted_traingle_pattern(n)
    triangle_start_pattern(n)


#     *
#    * *
#   *   *
#  *     *
# * * * * *
def hollow_traingle(n):
    x=1
    for i in range(n):
        print(" "*(n-i-1),end="")
        if i==(n-1):
            print("* "*(n))
        elif i==0:
            print("*"," "*(n-i-1))
        else:
            print("*"," "*x,"*",sep="")
            x+=2


# * * * * * 
#  *     *
#   *   *
#    * *
#     *    
def inverted_hollow_triangle(n):
    x=((n-2)*2)-1
    for i in range(n):
        print(" "*i,end="")
        if i==0:
            print("* "*n)
        elif i==n-1:
            print("*"+" "*(i))
        else:
            print("*"+" "*x+"*")
            x-=2

#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *
def diamond(n):
    x=1
    for i in range(2*n+1):
        print(" "*abs(n-i),end="")
        if i==0 or i==2*n:
            print("*")
        elif i<n:
            print("*"+" "*x+"*")
            x+=2
        elif i>=n:
            print("*"+" "*x+"*")
            x-=2


n=int(input("n:"))
inverted_pyramid(n)
inverted_traingle_pattern(n)
hour_glass(n)
hollow_traingle(n)
inverted_hollow_triangle(n)
diamond(n)