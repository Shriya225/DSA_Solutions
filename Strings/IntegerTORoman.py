# ⏱️ Time Complexity (TC)

# The list has 13 fixed elements

# Loop always runs 13 times

# 👉 TC = O(1) (constant time)

# 🧠 Space Complexity (SC)

# Extra space only for output string

# Roman length is bounded (max ≈ 15 chars)

# 👉 SC = O(1)

def intToRoman( num: int) -> str:
    l = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400],["D", 500],["CM", 900],["M", 1000]]
    ans=""
    for i in range(len(l)-1,-1,-1):
        cnt=num//l[i][1]
        ans+=l[i][0]*cnt
        num%=l[i][1]
    return ans
n=int(input("n:"))
print(intToRoman(n))