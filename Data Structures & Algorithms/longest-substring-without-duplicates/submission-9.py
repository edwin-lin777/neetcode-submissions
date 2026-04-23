class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        left = 0
        final = 0

        for right in range(len(s)):
            while s[right] in mySet:
                mySet.remove(s[left])
                left += 1
            mySet.add(s[right])
            final = max(final, right - left + 1)

        return final
        