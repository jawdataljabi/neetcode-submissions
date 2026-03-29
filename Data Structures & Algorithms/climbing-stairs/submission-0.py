class Solution:
    def climbStairs(self, n: int) -> int:
        # tabulation approach: bottom up whilst constructing a list we will then index
        # dp = [0] * (n + 1) # the reason for the + 1 is we will have dp[0] included as a basecase
        # dp[0] = 1
        # dp[1] = 1
        
        # # n = 5, (0, 2)
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2] # say i = 2, then d[1] + dp[0] = 2
        
        # return dp[n]


        # the tabulation approach can be optimized with O(1) space by using two variables instead of a whole list
        # notice how the i depends on i-1 and i-2, this means we can just store them into a variable

        one = two = 1 # these initially mimic dp[0] and dp[1]

        for i in range(2, n + 1): # don't forget n+1 because of dp[0]
            temp = two # this all here and below is literally like tabulation, but we are shifting two variable instead
            two = one + two
            one = temp
        return two
            