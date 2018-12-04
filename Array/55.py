class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farIndex = 0
        for i, num in enumerate(nums):
            if i > farIndex: return False
            farIndex = max(farIndex, i+num)
        return True
