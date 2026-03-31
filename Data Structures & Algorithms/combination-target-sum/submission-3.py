class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        subset = []

        def dfs(index, total):
            if total == target:
                output.append(subset.copy())
                return
            elif index >= len(nums) or total > target:
                return
            
            # decide to keep element
            subset.append(nums[index])
            dfs(index, total + nums[index])

            # decide not to keep it, and go to the next element
            subset.pop()
            dfs(index + 1, total)

        dfs(0, 0)
        return output
