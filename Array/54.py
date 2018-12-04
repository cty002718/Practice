class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        ans = []
        direction = 0
        limit = [len(matrix[0]) - 1, len(matrix) - 1, 0, 1]
        x, y = 0, 0
        num = len(matrix[0]) * len(matrix)
        while num:
            ans.append(matrix[x][y])
            if direction == 0:
                if y < limit[0]:
                    y += 1
                else:
                    x += 1
                    direction = 1
                    limit[0] -= 1
            elif direction == 1:
                if x < limit[1]:
                    x += 1
                else:
                    y -= 1
                    direction = 2
                    limit[1] -= 1
            elif direction == 2:
                if y > limit[2]:
                    y -= 1
                else:
                    x -= 1
                    direction = 3
                    limit[2] += 1
            elif direction == 3:
                if x > limit[3]:
                    x -= 1
                else:
                    y += 1
                    direction = 0
                    limit[3] += 1
            num -= 1

        return ans
