class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s = "XYYXZ"
        # freqDict = {"X": 1, "Y": 2, "Z": 1}
        # replacements = (right - left + 1) - max(freqDict)

        # 0, 1, 1, 2, 3 (however, this is NOT valid because replacements > k), 2

        # for incrementing the left pointer, the condition would be: while replacements > k, then do freqDict[left] -= 1, left += 1

        freqDict = {}
        left = 0
        output = 0

        for right in range(len(s)):
            freqDict[s[right]] = 1 + freqDict.get(s[right], 0)
            replacements = (right - left + 1) - max(freqDict.values())

            while replacements > k and left < right:
                freqDict[s[left]] -= 1
                left += 1
                replacements = (right - left + 1) - max(freqDict.values())
            
            output = max(output, right - left + 1)
        
        return output

