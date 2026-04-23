class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        left = 0
        final = 0

        for i in range(len(s)):
            while s[i] in mySet:
                mySet.remove(s[left])
                left += 1
            mySet.add(s[i])
            final = max(final, i - left + 1)
        return final
        