class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # the idea is to do a sliding window, both pointers starting
        # at the same spot. Then using a hashmap, we use the formula:
        # (length of window) - (max occurence) <= k
        left = 0
        right = 0
        maxLength = currentLength = 1
        letterOccurence = {} # will store amount of each letter for current window
        letterOccurence[s[left]] = 1 # add first letter to dict 

        while right < len(s):
            # this will give us the amount of letters to replace in current window
            if (right - left + 1) - max(letterOccurence.values()) <= k: 
                maxLength = max(maxLength, currentLength)
                if right == len(s) - 1:
                    break
                else:
                    currentLength += 1
                    right += 1
                if s[right] in letterOccurence:
                    letterOccurence[s[right]] += 1
                else:
                    letterOccurence[s[right]] = 1
            else:
                letterOccurence[s[left]] -= 1
                left += 1
                if currentLength == maxLength:
                    currentLength -= 1
                else:
                    currentLength -= 1

        return maxLength
