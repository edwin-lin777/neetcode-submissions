class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        final = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            while (r - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            final = max(final, r - left + 1)
        return final

