class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compDict = dict()
        for val in range(0, len(nums)):
            comp = target - nums[val]
            if(comp in compDict.keys()):
                return  [compDict[comp], val]
            else:
                compDict[nums[val]] = val       
        