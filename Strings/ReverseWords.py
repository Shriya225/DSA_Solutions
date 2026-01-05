
# 151. Reverse Words in a String
def revWords(s):
    s2=s.split()
    print(s2[::-1])
    print(list(s))
    return " ".join(s2)
s=input()
print(revWords(s))