class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we would have a dict
        # {(1, 0, 1, ...): ["cat", "act"], ...}
        # tuple positions would be the letter frequencies in order
        
        groups = {}

        for string in strs:
            letters = [0] * 26
            for index in range(len(string)):
                value = ord(string[index]) - ord("a")
                letters[value] += 1
            key = tuple(letters)
            if key in groups:
                groups[key].append(string)
            else:
                groups[key] = [string]
        
        return list(groups.values())


