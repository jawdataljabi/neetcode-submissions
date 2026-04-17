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

        output = []

        def dfs(index, curStr):
            if index >= len(digits):
                output.append(curStr)
                return

            for letter in mapDict[digits[index]]:
                newStr = curStr + letter
                dfs(index + 1, newStr)
        
        if digits:
            dfs(0, "")
        return output
            
                