class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        for tempIndex in range(len(temperatures)):
            for futureIndex in range(tempIndex + 1, len(temperatures)):
                if temperatures[futureIndex] > temperatures[tempIndex]:
                    output[tempIndex] = futureIndex - tempIndex
                    break
        
        return output






