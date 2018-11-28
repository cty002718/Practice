class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        length = len(nums)-1
        for i, num in enumerate(nums):
            if num > 0 or (i > 0 and nums[i-1] == num):
                continue
            left = i+1
            right = length
            while left < right:
                sum = nums[left] + nums[right]
                if sum > -num:
                    right -= 1
                elif sum < -num:
                    left += 1
                else:
                    find = [num, nums[left], nums[right]]
                    ans.append(find)
                    left += 1
                    right -= 1
                    while left <= length and nums[left] == nums[left-1]:
                        left += 1
                    while right >= 0 and nums[right] == nums[right+1]:
                        right -= 1

        return ans
        
