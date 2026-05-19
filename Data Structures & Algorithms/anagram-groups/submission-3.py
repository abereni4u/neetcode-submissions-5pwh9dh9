class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = dict()

        for string in strs:
            freqCounter = [0] * 26
            for ch in string:
                freqCounter[ord(ch) - ord('a')] += 1
            freqCounter = tuple(freqCounter)
            if(freqCounter in anaDict.keys()):
                anaDict[freqCounter].append(string)
            else:
                anaDict[freqCounter] = [string]

        return list(anaDict.values())