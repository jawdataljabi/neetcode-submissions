class Solution:
    def findMin(self, nums: List[int]) -> int:

        # nums = [1,2,3,4,5,6]

        # nums = [3,4,5,6,1,2]

        # nums = [4,5,0,1,2,3]

        # if left < right, then we break
        # if middle > left, then we do left = mid + 1
        # else we do right = mid - 1

        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res