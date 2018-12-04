class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        map = {}
        for i, num in enumerate(nums):
            if map.get(target-num, -1) >= 0:
                return [map[target-num], i]
            map[num] = i

