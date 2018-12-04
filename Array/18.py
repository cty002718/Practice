class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        length = len(nums)
        for i, num1 in enumerate(nums):
            if i > 0 and nums[i-1] == num1: continue
            if nums[i]*4 > target or nums[length-1]*4 < target: break
            for j in range(i+1, length):
                if j > i+1 and nums[j-1] == nums[j]: continue
                if nums[j]*3 + num1 > target or nums[length-1]*3 + num1 < target: break
                left, right = j + 1, length - 1
                while left < right:
                    summary = num1 + nums[j] + nums[left] + nums[right]
                    if summary > target:
                        right -= 1
                    elif summary < target:
                        left += 1
                    else:
                        found = [num1, nums[j], nums[left], nums[right]]
                        ans.append(found)
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]: left += 1
                        while left < right and nums[right] == nums[right+1]: right -= 1

        return ans
        
