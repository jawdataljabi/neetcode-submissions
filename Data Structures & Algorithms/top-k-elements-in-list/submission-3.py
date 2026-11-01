class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # could create a list of lists; let's call it freqList
        # each index in the list would be the number of times elements appear
        # within each index, there would be a list of numbers that appear "index" number of times (based off position)

        # for the example nums = [1,2,2,2,3,3,3]
        # freqList = [[1], [], [2,3]]

        freqDict = {} # key is number, value is frequency

        for num in nums:
            freqDict[num] = 1 + freqDict.get(num, 0)
        
        freqList = []

        for _ in range(len(nums)): # need to do this to avoid deep copies
            freqList.append([])

        for num in freqDict:
            freqList[freqDict[num] - 1].append(num)
        
        output = []

        for index in range(len(freqList) - 1, -1, -1):
            for num in freqList[index]:
                output.append(num)
                if len(output) == k:
                    return output
                
            
        