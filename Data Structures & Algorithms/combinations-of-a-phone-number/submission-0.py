class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        mapDict = {
            "2": "abc", 
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(index, curStr):
            # base case
            if len(curStr) == len(digits):
                output.append("".join(curStr))
                return
            
            for char in mapDict[digits[index]]:
                subStr = curStr + char # "d" + "g", "d" + "h", "d" + "i"
                dfs(index + 1, subStr)
            

        # must check in case digits is empty
        if digits:
            dfs(0, "")
        
        return output