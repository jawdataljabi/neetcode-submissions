class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # we want to store as value: index

        for index, num in enumerate(nums):
            complement = target - num # target - num = number we are looking for

            if complement in seen: # this means that we found the match where nums[i] + nums[j] == target
                if seen[complement] < index:
                    return [seen[complement], index]
                return [index, seen[complement]]
            seen[num] = index
        



