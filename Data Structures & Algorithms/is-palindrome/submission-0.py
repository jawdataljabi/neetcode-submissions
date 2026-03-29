class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for character in s:
            if character.isalnum():
                newString += character.lower()
        
        reversedString = "".join(reversed(newString))
        if newString == reversedString:
            return True
        return False