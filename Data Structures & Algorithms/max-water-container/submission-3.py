class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right = 0, len(heights) - 1
        maxSize = 0

        while left < right:
            size = min(heights[left],heights[right]) * (right - left)
            maxSize = max(size,maxSize)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxSize

        