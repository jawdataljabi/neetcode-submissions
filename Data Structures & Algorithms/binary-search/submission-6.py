import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # index = bisect.bisect_left(nums, target) # this finds index where x >= target
        # if index < len(nums) and nums[index] == target:
        #     return index
        # else:
        #     return -1

        # [-1,0,2,3,4,6,8]

        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] >= target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1 # the plus 1 will force left to equal right at some point
        if left < len(nums) and nums[left] == target:
            return left
        else:
            return -1
        
        



