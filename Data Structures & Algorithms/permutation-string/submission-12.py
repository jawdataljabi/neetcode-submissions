class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 = "abc
        # s2 = "lecabee"

        if len(s1) > len(s2):
            return False

        s1Dict = {}
        s2Dict = {}

        for char in s1:
            s1Dict[char] = 1 + s1Dict.get(char, 0)
        
        windowSize = len(s1)

        # create the window dict within s2
        for i in range(0, windowSize):
            s2Dict[s2[i]] = 1 + s2Dict.get(s2[i], 0)

        if s1Dict == s2Dict:
            return True
        
        # s1Dict = {"a": 1, "b": 1, "c": 1}
        # s2Dict = {"l": 1, "e": 1, "c": 1, "a": 1}

        left = 0
        for right in range(windowSize, len(s2)):
            s2Dict[s2[right]] = 1 + s2Dict.get(s2[right], 0)

            s2Dict[s2[left]] -= 1
            if s2Dict[s2[left]] == 0:
                del s2Dict[s2[left]]
            left += 1

            if s1Dict == s2Dict:
                return True
        
        return False




        

        