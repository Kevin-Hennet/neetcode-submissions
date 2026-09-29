class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        attempt before conceptual 
        need to find the max possible area 
        l = 0 
        r = len(heights) - 1
        width = r - l 
        height = min(l, r)
        area = width * height 
        while (l < r):
            if ()
        """
        res = 0 
        l = 0 
        r = len(heights) -1 
        while (l < r): 
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)
            if heights[l] < heights[r]: 
                l += 1 
            else: 
                r -= 1 
        return res

            