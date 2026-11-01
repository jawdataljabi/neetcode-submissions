class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums =    [1,2,4,6]
        # prefix =  [1,1,2,8]    -> everything to the left of an element
        # postfix = [48,24,6,1]  -> everything to the right of an element

        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        for index in range(len(nums)):
            if not index:
                prefix[index] = 1
            else:
                prefix[index] = prefix[index - 1] * nums[index - 1]
        
        for index in range(len(nums) - 1, -1, -1):
            if index == len(nums) - 1:
                postfix[index] = 1
            else:
                postfix[index] = postfix[index + 1] * nums[index + 1]
        
        output = [0] * len(nums)

        for index in range(len(nums)):
            output[index] = prefix[index] * postfix[index]
        
        return output

