class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        table = {}
        
        for i, n in enumerate(nums):
            r = target - n
            if r in table:
                return [table[r], i]
            table[n] = i
        return []
