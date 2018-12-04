class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]
        ans = [-1, -1]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1

        if nums[r] == target: ans[0] = r

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2 + 1
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] <= target:
                l = mid

        if nums[l] == target: ans[1] = l
        return ans
