class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = dict()
        bucketArray = [[] for _ in range (len(nums) + 1)]

        for num in nums:
            freqCount.setdefault(num, 0)
            freqCount[num] += 1
        
        for key in freqCount.keys():
            bucketArray[freqCount[key]].append(key)
        
        resultArray = []
        for val in range (len(bucketArray) - 1, -1, -1):
            for item in bucketArray[val]:
                resultArray.append(item)
                if(len(resultArray) == k):
                    return resultArray
        