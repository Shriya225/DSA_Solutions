# class Person:
#     def __init__(self,n):
#         self.name=n
#     def greet(self):
#         print(self.name,":::::s")
# p=Person("shri")
# print(p.name)
# p.greet()

# def replace_vowels(s):
#     ans=''
#     d=dict()
#     for i in range(len(s)):
#         if s[i] in "aeiou":
#             d[s[i]]=d.get(s[i],0)+1
#             if d[s[i]]==2:
#                 ans+="#"
#             else:
#                 ans+=s[i]
#         else:
#             ans+=s[i]

# s=input()
# print(replace_vowels(s))


def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
n=int(input("n:"))
print(fact(n))