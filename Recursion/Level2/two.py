# def atoi(s,l,i=0):
#     if l<0:
#         return 0
#     return ((ord(s[l])-ord('0'))*10**(i))+atoi(s,l-1,i+1)
# s=input()
# print(atoi(s,len(s)-1))

# def atoi2(s,l):
#     if l==-1 or s[l]==" ":
#         return 0
#     return (ord(s[l])-ord('0'))+10*(atoi2(s,l-1))

# s=input()
# print(atoi2(s,len(s)-1))


# left to right approach
# -000123
def atoi(s, i=0, value=0, sign=1):

    # Step 1: skip spaces
    if i < len(s) and s[i] == ' ':
        return atoi(s, i+1, value, sign)

    # Step 2: sign
    if i < len(s) and (s[i] == '-' or s[i] == '+'):
        sign = -1 if s[i] == '-' else 1
        return atoi(s, i+1, value, sign)

    # Step 4: stop at non-digit
    if i >= len(s) or not s[i].isdigit():
        return sign * value

    # Step 3: build value left→right
    d = ord(s[i]) - ord('0')
    value = value * 10 + d

    # Move forward
    return atoi(s, i+1, value, sign)


s=input()
print(atoi(s))