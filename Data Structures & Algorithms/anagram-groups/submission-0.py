class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencyDict = {}
        # having the keys as tuples which represent the occurences
        # then I would have the values as the strings which the tuple corresponds to

        for string in strs:
            frequencyList = [0] * 26 # [0,0,0,0,0,...] 26 times
            # what ord function does is it converts character to designated ascii value
            for character in string:
                characterIndex = ord(character) - ord("a") # using "a" as the starting point 
                frequencyList[characterIndex] += 1
            frequencyTuple = tuple(frequencyList) # since tuples are hashable (lists are not)
            if frequencyTuple in frequencyDict:
                frequencyDict[frequencyTuple].append(string)
            else:
                frequencyDict[frequencyTuple] = [string]
        
        
        return list(frequencyDict.values()) # make sure to convert to a list since it returns a view object. 
                                            # The view object contains the values of the dictionary, as a list.
            
