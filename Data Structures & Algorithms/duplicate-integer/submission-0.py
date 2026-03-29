class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        elementsSeen = {}
        for num in nums:
            if num not in elementsSeen:
                elementsSeen[num] = True
            elif num in elementsSeen:
                return True
        return False