class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "abbcadcad"
        left = 0 
        right = 1
        longestString = 0
        currentString = 0
        charactersSeen = set()

        if s:
            charactersSeen.add(s[left])
            longestString = currentString = 1

        while right < len(s):
            while s[right] in charactersSeen and left <= right:
                charactersSeen.remove(s[left])
                currentString -= 1
                left += 1
            while s[right] not in charactersSeen:
                charactersSeen.add(s[right])
                currentString += 1
                if right != len(s) - 1:
                    right += 1
                else:
                    longestString = max(longestString, currentString)
                    return longestString
                longestString = max(longestString, currentString)

        return longestString







