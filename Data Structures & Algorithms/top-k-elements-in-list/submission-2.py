class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # step 1:
        # create a dict, where key is number and value is the frequency
        # {1: 1, 2: 2, 3: 3, 7: 3}

        # step 2:
        # create a frequency list, where each index is the frequency - 1
        # freqList = [[1], [2], [3,7]]
        
        # step 3:
        # iterate through freqList backwards while appending to a final list k times

        freqDict = {}

        for num in nums:
            freqDict[num] = 1 + freqDict.get(num, 0)
        
        freqList = []

        for _ in range(len(nums)):
            freqList.append([])

        for num, freq in freqDict.items():
            freqList[freq - 1].append(num)


        output = []

        for index in range(len(freqList) - 1, -1, -1):
            for num in freqList[index]:
                output.append(num)
                if len(output) == k:
                    return output


        
