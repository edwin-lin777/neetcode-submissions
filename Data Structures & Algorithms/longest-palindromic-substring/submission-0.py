class Solution:
    def longestPalindrome(self, s: str) -> str:
        count = 0
        final = ""

        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right >=0 and left < len(s) and right < len(s) and s[left] == s[right]:
                if right - left + 1 > count:
                    final = s[left: right + 1]
                    count = right - left + 1
                right += 1
                left -= 1
            left = i
            right = i + 1
            while left >= 0 and right >= 0 and left < len(s) and right < len(s) and s[left] == s[right]:
                if right - left + 1 > count:
                    final = s[left: right + 1]
                    count = right - left + 1
                right += 1
                left -= 1
        return final
            



            
