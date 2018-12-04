class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            if i == 0: ans += 1
            elif nums[i] != nums[i-1]:
                nums[ans] = nums[i]
                ans += 1
        return ans
