#57. Insert Interval
class Solution:
    def insert(self, intervals) :
        i = 0
        ans=[]
        n = len(intervals)

        # before
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        # overlap
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # add merged interval
        ans.append(newInterval)

        # after
        while i < n:
            ans.append(intervals[i])
            i += 1
        return ans
