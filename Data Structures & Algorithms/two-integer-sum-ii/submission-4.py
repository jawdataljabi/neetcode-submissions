class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # can use two pointer approach 
        # if target > addition, move right pointer down
        # otherwise move left pointer up
        left = 0
        right = len(numbers) - 1

        while left < right:
            value = numbers[left] + numbers[right]

            if value == target:
                return [left + 1, right + 1]
            elif value < target:
                left += 1
            else:
                right -= 1
        