import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rates = range(1, max(piles) + 1) # all possible rates (will use binary search on this list and iterate through piles)
        left = 0
        right = len(rates) - 1
        k = max(piles) #  bananas-per-hour eating rate

        while left <= right:
            middle = (right + left) // 2 # middle is the rate we are currently looking at
            hours = 0 # hours it takes to eat all bananas with current rate

            for pile in piles:
                hours += math.ceil(pile/rates[middle]) # rounding up division due to constraints
            if hours <= h and rates[middle] < k:
                k = rates[middle] # update rate
                right = middle - 1
            else:
                left = middle + 1
        return k
