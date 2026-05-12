# Longest Bitonic subsequence (GFG)

# Brute

# reccurence rel'n
class Solution:
    def longestBitonicSequence(self, n, a):

        def lbs(a, i, prev, phase):

            if i == len(a):
                if phase == 1:
                    return 0
                return -10**9

            # skip
            not_take = lbs(a, i + 1, prev, phase)

            take = -10**9

            # increasing phase
            if phase == 0:

                # continue increasing
                if prev == -1 or a[i] > a[prev]:
                    take = 1 + lbs(a, i + 1, i, 0)

                # start decreasing
                if prev != -1 and a[i] < a[prev]:
                    take =  1 + lbs(a, i + 1, i, 1)

            # decreasing phase
            else:

                if a[i] < a[prev]:
                    take = 1 + lbs(a, i + 1, i, 1)

            return max(take, not_take)
        x=lbs(a, 0, -1, 0) 
        return x if x>=0 else 0
    

# this method meomizatio nwill take us to 3D Dp...
# tc-o(n^2),scO(n^2)
# so optiaml approach is using LIS method over ths pick or not pick..





    
