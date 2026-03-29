class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        str2 = {}
        for letter in s:
            if letter in str1:
                str1[letter] += 1
            else:
                str1[letter] = 1
        for letter in t:
            if letter in str2:
                str2[letter] += 1
            else:
                str2[letter] = 1
        if str1 == str2:
            return True
        return False
