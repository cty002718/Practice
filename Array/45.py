class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        end = 0
        nextEnd = 0
        last = len(nums) - 1
        for i, num in enumerate(nums):
            if end >= last:
                break
            nextEnd = max(nextEnd, i+num)
            if i == end:
                end = nextEnd
                count += 1
        return count
