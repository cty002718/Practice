class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        ans = [[float("inf")] * (n+1) for _ in range(m+1)]
        ans[m][n-1] = 0
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                ans[i][j] = min(ans[i+1][j], ans[i][j+1]) + grid[i][j]
        
        return ans[0][0]
