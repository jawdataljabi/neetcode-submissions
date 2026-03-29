class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        output = 0
        left = 0

        # s = "zxyzbca"

        # s = "zxyzzbca"

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            output = max(output, right - left + 1)
        
        return output