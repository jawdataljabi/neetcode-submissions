class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # can use two pointers
        # for each position, compute width x height
        # keep track of highest global value
        # move left/right pointers based off whichever one has a smaller height

        left = 0 
        right = len(heights) - 1

        output = 0

        while left < right:
            height = min(heights[left], heights[right])
            length = right - left
            output = max(output, height * length)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return output
