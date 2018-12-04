class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        ans = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[ans] = num
                ans += 1

        return ans
