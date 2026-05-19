class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeString = []
        for estr in strs:
            estrLen = list(str(len(estr)))
            for chLen in estrLen:
                encodeString.append(chLen)    
            encodeString.append('#')
            for ch in estr:
                encodeString.append(ch)
        encodeString = "".join(encodeString)
        return encodeString

    def decode(self, s: str) -> List[str]:
        resultArray = []
        while s != "":
            intString = []
            dString = []
            while s != "" and s[0] != '#':
                intString.append(s[0])
                s = s[1:]
            intString = int("".join(intString))
            s = s[1:]
            while s != "" and intString > 0:
                dString.append(s[0])
                intString -= 1
                s = s[1:]
            dString = "".join(dString)
            resultArray.append(dString)
        return resultArray