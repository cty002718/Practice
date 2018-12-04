class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        M = len(matrix)
        N = len(matrix[0])
        curD = (0, 1)
        res = []
        iBound = [1, M - 1]
        jBound = [0, N - 1]
        i, j = 0, 0
        for k in range(M * N):
            res.append(matrix[i][j])
            if curD[0] == 0: # horizontally
                if curD[1] == 1:
                    if j == jBound[1]:
                        jBound[1] -= 1
                        curD = (1, 0)
                else:
                    if j == jBound[0]:
                        jBound[0] += 1
                        curD = (-1, 0)
            else: # vertically
                if curD[0] == 1:
                    if i == iBound[1]:
                        iBound[1] -= 1
                        curD = (0, -1)
                else:
                    if i == iBound[0]:
                        iBound[0] += 1
                        curD = (0, 1)
            i += curD[0]
            j += curD[1]
        return res
