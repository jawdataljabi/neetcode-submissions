class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # [-4, -4, -1, -1, 0, 1, 2, 2]
        ref = 0
        left = 1
        right = len(nums) - 1
        result = []

        while left < right:
            currentVal = nums[ref] + nums[left] + nums[right]
            if currentVal < 0:
                left += 1
            elif currentVal > 0:
                right -= 1
            else:
                result.append([nums[ref], nums[left], nums[right]])
                oldLeft = nums[left]
                oldRight = nums[right]
                while nums[left] == oldLeft and left < right:
                    left += 1
                while nums[right] == oldRight and left < right:
                    right -= 1
            
            if left == right:
                ref += 1
                while nums[ref] == nums[ref - 1] and ref < len(nums) - 2:
                    ref += 1
                left = ref + 1
                right = len(nums) - 1
            
            if ref == right:
                break
        
        return result
            
                
                

            

