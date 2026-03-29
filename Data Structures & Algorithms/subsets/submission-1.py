class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []

        def dfs(index):
            if index >= len(nums):
                output.append(subset.copy())
                return
            
            # the decision to include nums[index]
            subset.append(nums[index])
            dfs(index+1)

            # the decision to exclude nums[index]
            subset.pop()
            dfs(index+1)
    
        dfs(0)
        return output
