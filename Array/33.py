class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: return -1
        left, right = 0, len(nums)
        pivot = nums[right-1]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > pivot and target <= pivot: left = mid + 1
            elif nums[mid] <= pivot and target > pivot: right = mid - 1
            elif target > nums[mid]: left = mid + 1
            elif target < nums[mid]: right = mid - 1
            else: return mid
        return -1
