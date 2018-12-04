class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [[0] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                if x and y:
                    memo[x][y] = memo[x-1][y] + memo[x][y-1]
                    continue
                memo[x][y] = 1
                    
        return memo[-1][-1]
