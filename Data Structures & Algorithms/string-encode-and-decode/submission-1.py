class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for word in strs:

            final += str(len(word)) + "#" + word
        return final




    def decode(self, s: str) -> List[str]:
        i = 0;
        final = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            final.append(s[j + 1: j + 1 + length])

            i = length + 1 + j



        return final