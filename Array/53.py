class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -float("inf")
        small = 0
        summary = 0
        for i in range(len(nums)):
            summary += nums[i]
            ans = max(ans, summary - small)
            small = min(small, summary)

        return ans
