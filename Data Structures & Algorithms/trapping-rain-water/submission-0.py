class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right] 
                    # purpose of these are to act as our boundaries
                    # we will end up moving the left and right pointers based off of whichever one has a smaller max value 
                    # to compute the rain at a certain pointer position, we will use the equation: min(maxLeft, maxRight) - height[pointer]
        rain = 0
       
        while left < right:
            if maxLeft <= maxRight:
                left += 1 # so now at this position, we want to compute the rain stored
                maxLeft = max(height[left], maxLeft)
                rain += maxLeft - height[left] # using int will round up to 0
                
            elif maxLeft > maxRight:
                right -= 1
                maxRight = max(height[right], maxRight)
                rain += maxRight - height[right]
    
        return rain



        
        
        
        # maxLeft = 1
        # maxRight = 3
        # rain = min(1, 3) - 0 = 1