# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if not intervals: return []
        intervals.sort(key=lambda x: (x.start, x.end))
        ans = []
        start = intervals[0].start
        end = intervals[0].end
        for interval in intervals[1:]:
            if interval.start <= end:
                end = max(end, interval.end)
            else:
                ans.append(Interval(start,end))
                start = interval.start
                end = interval.end
        ans.append(Interval(start,end))
        return ans
