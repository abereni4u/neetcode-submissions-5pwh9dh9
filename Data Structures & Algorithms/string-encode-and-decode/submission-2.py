class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)


    def decode(self, s: str) -> List[str]:
        # Get the length of each string before the #
        # Instead of using slicing which creates a new string everytime and is an O(n) operation
        # --use a pointer instead

        j = 0
        decoded = []
        while(j < len(s)):
            boundary = s.index("#", j)
            length = int(s[j:boundary])
            dWord = s[boundary + 1: boundary + 1 + length]
            decoded.append(dWord)
            j = boundary + 1 + length
            
        return decoded