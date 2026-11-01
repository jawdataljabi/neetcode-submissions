class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        str2 = {}

        for char in s:
            str1[char] = 1 + str1.get(char, 0) 

        for char in t:
            str2[char] = 1 + str2.get(char, 0)
        
        return str1 == str2