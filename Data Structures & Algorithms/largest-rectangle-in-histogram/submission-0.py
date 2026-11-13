class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack:List[int] = []
        max_ar = 0
        n =len(heights)
        for i in range(n+1):
            curr_ht = 0 if i ==n else heights[i]
            while stack and heights[stack[-1]] > curr_ht:
                popid = stack.pop()
                rec_h = heights[popid]
                left_smaller_idx = stack[-1] if stack else -1
                rec_w = i- left_smaller_idx -1
                ar = rec_h * rec_w
                if ar > max_ar:
                    max_ar = ar
            stack.append(i)
        return max_ar