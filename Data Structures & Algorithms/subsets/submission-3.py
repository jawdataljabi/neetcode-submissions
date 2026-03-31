class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # we are going to have a subset list which is changed then copied when we add it
        # we are also going to have an output list for final result

        output = []
        subset = []

        def dfs(index):
            # add element
            # call fn
            # remove element
            # call fn

            # [1,2,3]

            # base case
            if index >= len(nums):
                output.append(subset.copy())
                return

            # add element and then call
            subset.append(nums[index])
            dfs(index + 1)

            # call without adding
            subset.pop()
            dfs(index + 1)
        
        dfs(0)
        return output



