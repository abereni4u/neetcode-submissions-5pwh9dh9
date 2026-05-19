class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = dict()
        for num in nums:
            if num in freqDict.keys():
                freqDict[num] += 1
            else:
                freqDict[num] = 1
        
        bucketArray = [ [] for _ in range(len(nums) + 1) ]

        for key in freqDict.keys():
            bucketArray[freqDict[key]].append(key)
        
        resultArray = []
        
        for val in range(len(bucketArray)-1, -1, -1):
            for n in bucketArray[val]:
                resultArray.append(n)
                if(len(resultArray) == k):
                    return resultArray
