class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {key1: ["act", "cat"], key2: ["stop", "pots"]}
        # "badd"
        # maximum of 26 letters in the alphabet
        # [0,0,0,0]
        # [1,1,0,2]

        freqDict = {}

        for string in strs:
            letterList = [0] * 26
            for letter in string:
                letterIndex = ord(letter) - ord("a")
                letterList[letterIndex] += 1
            letterTuple = tuple(letterList)
            if letterTuple in freqDict:
                freqDict[letterTuple].append(string)
            else:
                freqDict[letterTuple] = [string]

        return list(freqDict.values())