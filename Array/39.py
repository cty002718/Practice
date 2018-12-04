class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        length = len(candidates)
        def solve(index, nowList, remain):
            if remain == 0:
                ans.append(nowList.copy()) 
                return
            for i in range(index, length):
                if candidates[i] <= remain:
                    nowList.append(candidates[i])
                    solve(i, nowList, remain - candidates[i])
                    nowList.pop()
        solve(0, [], target)
        return ans
