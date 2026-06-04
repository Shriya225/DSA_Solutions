# 4 June 2026
# 3751. Total Waviness of Numbers in Range I

# Brute
def waviness(a,b):
    ans=0
    for i in range(a,b+1):
        s=str(i)
        for j in range(1,len(s)-1):
            if s[j-1]<s[j]>s[j+1] or s[j-1]>s[j]<s[j+1]:
                ans+=1
    return ans
print(waviness(120,130))


# Digit Dp

