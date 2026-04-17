class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        str2 = {}
        for letter in s:
            str1[letter] = 1 + str1.get(letter, 0)
        for letter in t:
            str2[letter] = 1 + str2.get(letter, 0)

        if str1 == str2:
            return True
        return False