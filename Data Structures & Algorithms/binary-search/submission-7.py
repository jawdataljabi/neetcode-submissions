import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # index = bisect.bisect_left(nums, target) # this finds index where x >= target
        # if index < len(nums) and nums[index] == target:
        #     return index
        # else:
        #     return -1

        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if nums[middle] >= target:
                right = middle 
            elif nums[middle] < target:
                left = middle + 1 # this is the crucial part; say the middle ends up being the target, then we set right there,
                                  # then this will be the block that will keep running, which ends up making left = right
        return left if left < len(nums) and nums[left] == target else -1
        
        
        



