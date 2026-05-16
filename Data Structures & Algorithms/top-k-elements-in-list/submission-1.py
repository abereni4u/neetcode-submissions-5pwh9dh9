class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = dict()
        outList = []
        for num in nums:
            if(num in freqDict.keys()):
                freqDict[num] += 1
            else:
                freqDict[num] = 1
        while(k > 0):
            largestVal = 0
            largestKey = 0
            for key in freqDict.keys():
                if(freqDict[key] > largestVal):
                    largestVal = freqDict[key]
                    largestKey = key
            outList.append(largestKey)
            k -= 1
            freqDict.pop(largestKey)
    
        return outList