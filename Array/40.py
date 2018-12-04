class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        length = len(candidates)
        def solve(index, nowList, remain):
            if remain == 0:
                ans.append(nowList.copy()) 
                return
            for i in range(index, length):
                if i > 0 and candidates[i] == candidates[i-1] and i > index:
                    continue
                if candidates[i] <= remain:
                    nowList.append(candidates[i])
                    solve(i+1, nowList, remain - candidates[i])
                    nowList.pop()
        solve(0, [], target)
        return ans
