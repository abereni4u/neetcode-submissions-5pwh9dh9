class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = nums.count(0)
        zeroPresent = False
        outputArray = []
        if(zeroCount > 1):
            return [0] * len(nums)
        else:
            if zeroCount == 1:
                zeroPresent = True
            
            product = 1

            for val in nums:
                if val != 0:
                    product *= val
            
            for val in nums:
                if zeroPresent and val != 0:
                    outputArray.append(0)
                elif zeroPresent and val == 0:
                    outputArray.append(product)
                else:
                    outputArray.append(product // val)
            
            return outputArray 