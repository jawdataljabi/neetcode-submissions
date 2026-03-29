class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tripletArray = []
        nums.sort() # sort the array from decreasing to increasing... ex: [-4, -1, -1, -1, 0, 1, 2]

        right = len(nums) - 1
        target = 0
        left = 1


        while left < right:
            outcome = nums[left] + nums[right] + nums[target]
            if outcome < 0:
                left += 1
            elif outcome > 0:
                right -= 1
            else:
                tripletArray.append([nums[left], nums[target], nums[right]])
                oldLeft = nums[left]
                oldRight = nums[right]
                while nums[left] == oldLeft and left < right:
                    left += 1
                while nums[right] == oldRight and left < right:
                    right -= 1

            if right == left:
                target += 1
                while nums[target] == nums[target - 1] and target < len(nums) - 2:
                    target += 1
                left = target + 1
                right = len(nums) - 1
            
            if target == right:
                break
        
        return tripletArray


