class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        record = [[0 for i in range(n+m)] for i in range(n+m)]
        for i in range(n+m-1):
            record[i][0] = 1
        for i in range(1, n+m-1):
            for j in range(1, n+m-1):
                record[i][j] = record[i-1][j-1] + record[i-1][j]
        return record[n+m-2][n-1]
