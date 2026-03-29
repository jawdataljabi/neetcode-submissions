class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [] # final result
        subset = [] # variable for each subset

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy()) # super important because subset will change eventually
                return
            
            # the case where we add include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # the case where we don't include nums[i]
            subset.pop() # the reason we pop is to remove the element we just added, which is the same as never adding it to begin with
            dfs(i + 1)

        dfs(0) # the first instance of the function at index 0
        return result