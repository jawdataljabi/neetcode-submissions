class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        output = [] # this is what we will return

        def dfs(index, curStr):
            # base case
            if len(curStr) == len(digits):
                output.append(curStr)
                return
            
            for char in mapDict[digits[index]]:
                subStr = curStr + char
                dfs(index + 1, subStr)
        
        if digits:
            dfs(0, "")
        return output
            


        