class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums) - 1
        idx = length
        while idx > 0 and nums[idx] <= nums[idx-1]: idx -= 1
        
        right = length
        left = idx
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        if idx > 0:
            tmp = idx
            idx -= 1
            while nums[tmp] <= nums[idx]: tmp += 1
            nums[tmp], nums[idx] = nums[idx], nums[tmp]

