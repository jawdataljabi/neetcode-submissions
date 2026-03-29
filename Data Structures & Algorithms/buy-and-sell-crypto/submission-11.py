class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        output = 0

        # [10,1,5,6,7,1]

        while right < len(prices):
            if prices[left] < prices[right]:
                output = max(output, prices[right] - prices[left])
                right += 1
            else: # this is when left is greater or equal to right
                left = right
                right = left + 1
        
        return output

