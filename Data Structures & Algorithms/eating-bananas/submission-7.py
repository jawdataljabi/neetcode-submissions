class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h = number of hours we have to eat all the bananas
        # k = rate per hour of eating bananas

        # we want to return the minimum k (rate)
        # k max = max(piles)
        # k min = ?

        # piles = [1,4,3,2], h = 9
        # k = [1,2,3,4]
        # if the current k value is <= h, then we could shift the right pointer to mid - 1

        k = range(1, max(piles) + 1)

        left = 0
        right = len(k) - 1

        output = 0

        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k[mid]) # this gives the hours per pile with the given k rate "mid"
            if hours <= h:
                output = k[mid]
                right = mid - 1
            else: # this is when hours > h (not valid so shift left pointer)
                left = mid + 1
        
        return output




