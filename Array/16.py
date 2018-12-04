class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        gap = float("inf")
        for i, num in enumerate(nums):
            t = target - num
            left = i + 1
            right = length - 1
            while left < right:
                summary = nums[left] + nums[right]
                if summary > t:
                    if abs(summary-t) < gap:
                        ans = summary + num
                        gap = abs(summary-t)
                    right -= 1
                elif summary < t:
                    if abs(summary-t) < gap:
                        ans = summary + num
                        gap = abs(summary-t)
                    left += 1
                else:
                    return target
        return ans
