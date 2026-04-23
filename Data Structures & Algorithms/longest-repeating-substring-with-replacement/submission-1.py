class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mySet = {}
        left = 0
        final = 0
        for r in range (len(s)):
            mySet[s[r]] = mySet.get(s[r], 0) + 1
            if r - left + 1  - max(mySet.values())> k:
                mySet[s[left]] = mySet.get(s[left], 0) - 1
                left += 1
            final = max(final, r - left + 1)

        return final
