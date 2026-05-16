class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = dict()
        for string in strs:
            alphArray = [0] * 26
            for ch in string:
                alphArray[ord('a') - ord(ch)] += 1
            alphTuple = tuple(alphArray)

            if(alphTuple in anagramDict.keys()):
                anagramDict[alphTuple].append(string)
            else:
                anagramDict[alphTuple] = [string]
        
        return list(anagramDict.values())
