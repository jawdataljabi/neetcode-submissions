class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index in range(len(nums)):
            complement = target - nums[index] # complement here is the value we are looking for inside of the list
            if complement in dictionary:
                return [dictionary[complement], index]
            dictionary[nums[index]] = index