class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,11,4,5,1,5,3,7,6,1]
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            maxProfit = max(currentProfit, maxProfit)
            if prices[right] < prices[left]:
                left = right
            right += 1
        return maxProfit