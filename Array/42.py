class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        maximum = -1
        for i, h in enumerate(height):
            if h > maximum:
                maximum = h
                position = i

        ans = 0
        tmpsum = 0
        now_position = 0
        now_height = 0
        for i, h in enumerate(height):
            if i > position: break
            elif h >= now_height:
                ans += (i - now_position - 1) * now_height - tmpsum
                tmpsum = 0
                now_position = i
                now_height = h
            else:
                tmpsum += h

        tmpsum = 0
        now_position = 0
        now_height = 0
        for i in range(len(height)-1, -1, -1):
            if i < position: break
            elif height[i] >= now_height:
                ans += (now_position - i - 1) * now_height - tmpsum
                tmpsum = 0
                now_position = i
                now_height = height[i]
            else:
                tmpsum += height[i]
        return ans
