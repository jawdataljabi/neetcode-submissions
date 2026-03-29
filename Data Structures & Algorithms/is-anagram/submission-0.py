class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        stringOne = {}
        stringTwo = {}

        for char in s:
            if char not in stringOne:
                stringOne[char] = 1
            elif char in stringOne:
                stringOne[char] += 1
        for char in t:
            if char not in stringTwo:
                stringTwo[char] = 1
            elif char in stringTwo:
                stringTwo[char] += 1
        if stringOne == stringTwo:
            return True
        return False
