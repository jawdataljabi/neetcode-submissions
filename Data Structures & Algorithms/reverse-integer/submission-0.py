class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2147483647
        MIN = -2147483648

        result = 0

        while x:
            lastDigit = int(math.fmod(x,10)) # get the last digit to potentially compare
            x = int(x/10) # not floor division since we want to go towards 0 for removing digit

            if (result > MAX // 10) or (result == MAX // 10 and lastDigit > MAX % 10):
                return 0
            if (result < MIN // 10) or (result == MIN // 10 and lastDigit < MAX % 10):
                return 0
            result = (result * 10) + lastDigit 
        return result


        # time: log(x)
