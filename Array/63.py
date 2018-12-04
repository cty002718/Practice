class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        ans = [[0] * (len(obstacleGrid[0])+1) for _ in range(len(obstacleGrid)+1)]
        ans[len(obstacleGrid)][len(obstacleGrid[0])-1] = 1
        for i in range(len(obstacleGrid)-1, -1, -1):
            for j in range(len(obstacleGrid[0])-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    ans[i][j] = 0
                else:
                    ans[i][j] = ans[i+1][j] + ans[i][j+1]
        return ans[0][0]
