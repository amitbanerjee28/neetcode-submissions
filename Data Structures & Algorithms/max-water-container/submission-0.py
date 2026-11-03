class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left =0
        right = len(heights) -1
        max_water = 0
        while left < right :
            h_left = heights[left]
            h_right = heights[right]
            current_water = (right -left) * min(h_left,h_right)
            if current_water > max_water:
                max_water = current_water
            if heights[left] < heights[right]:
                while left < right and heights[left] <= h_left:
                    left +=1
            else:
                while left < right and heights[right]<= h_right:
                    right -=1
        return max_water
                 