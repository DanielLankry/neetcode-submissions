class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mostWater = 0
        l = 0
        r = len(heights) - 1

        while l < r:
             waterSum = min(heights[l], heights[r]) * (r - l)
             mostWater = max(mostWater, waterSum)

             if heights[l] < heights[r]:
                   l += 1
             else:
                   r -= 1

                
        return int(mostWater)



        