class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = right = 0
        first = {}
        clone = {}

        for i in s1:
            if i in first:
                first[i] += 1
            else:
                first[i] = 1

        while right < len(s2):
            #lecaeabc
            #eee
            if s2[right] not in first and right < len(s2) - 1:
                right += 1
                left = right
                clone = {}

            elif s2[right] in first and right - left <= len(s1) - 1:
                if s2[right] in clone:
                    clone[s2[right]] += 1
                else:
                    clone[s2[right]] = 1
                if right - left != len(s1) - 1:
                    right += 1
                else:
                    if first == clone:
                        return True
                    else:
                        clone[s2[left]] -= 1
                        left += 1
                        right += 1
            elif first != clone and right == len(s2) - 1:
                return False

        return False
                



            

                