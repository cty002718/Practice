class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        maxArea=0
        while left < right:
            w = right - left
            if height[left] < height[right]:
                h = height[left]
                left+=1
            else:
                h = height[right]
                right-=1
            maxArea = max(maxArea, h*w)

        return maxArea
