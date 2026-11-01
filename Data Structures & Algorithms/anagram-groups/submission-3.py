class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # can use ord to find the number of times each letter appears
        # would store the ord tuple as a key in a dict, and the value would be the strings that match the ord tuple 

        output = []
        matches = {} # key: ord list, value: list of strings

        for string in strs:
            letters = [0] * 26 # there are only 26 letters in the alphabet

            for char in string:
                charIndex = ord(char) - ord("a") # to get index
                letters[charIndex] += 1
            
            key = tuple(letters) # since lists cannot be dict keys
            
            if key in matches:
                matches[key].append(string)
            else:
                matches[key] = [string]
        
        for anagrams in matches.values():
            output.append(anagrams)

        return output
