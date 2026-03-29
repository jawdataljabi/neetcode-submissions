class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums = [2,5,6,9]
        output = []
        subset = []

        def dfs(i, subset, total):
            if total == target:
                output.append(subset.copy())
                return
            elif i >= len(nums) or total > target:
                return # no match was found
            
            # decision to include the index i
            subset.append(nums[i])
            dfs(i, subset, total + nums[i])

            # decision not to include the index i
            subset.pop() # this removes index i (since it was added in previous decision)
            dfs(i+1, subset, total)
        
        dfs(0, subset, 0)
        return output

        