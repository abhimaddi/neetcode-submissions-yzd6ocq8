class Solution:
    def maxArea(self, heights: List[int]) -> int:
        sol = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            area = (right-left) * min(heights[left], heights[right])
            sol = max(sol,area)
            if(heights[left] < heights[right]):
                left += 1
            elif(heights[right] > heights[left]):
                right -= 1
            else:
                right -= 1
        return sol

