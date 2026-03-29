class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}

        # nums = [1,2,2,3,3,3,7,7,7]
        # freqList = [[1],[2],[3,7]]

        for number in nums:
            freqDict[number] = 1 + freqDict.get(number, 0)
        
        freqList = []

        for _ in range(len(nums)):
            freqList.append([])

        for num, freq in freqDict.items():
            freqList[freq - 1].append(num)

        finalList = []

        for index in range(len(freqList) - 1, -1, -1):
            for number in freqList[index]:
                finalList.append(number)
                if len(finalList) == k:
                    return finalList
        



# {7: 3}
