class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for each element, we can find the complement
        # the complement is target - curElement, since that would achieve the target

        seen = {} # key is number, value is index

        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in seen:
                return [seen[complement], index]
            seen[nums[index]] = index