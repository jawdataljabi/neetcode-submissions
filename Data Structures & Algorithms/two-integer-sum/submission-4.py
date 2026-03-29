class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # Will contain indexes and elements

        for index, num in enumerate(nums):
            hashmap[num] = index
        for i in range(len(nums)):
            desiredNumber = target - nums[i] # IMPORTANT PART OF THE PROBLEM HERE
            if desiredNumber in hashmap and i != hashmap[desiredNumber]:
                return [i, hashmap[desiredNumber]]


