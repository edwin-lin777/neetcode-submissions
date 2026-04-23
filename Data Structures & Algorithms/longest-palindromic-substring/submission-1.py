class Solution:
    def longestPalindrome(self, s: str) -> str:
        count = 0
        final = ''
        

        for i in range(len(s)):
            l = i
            r = i
            while l>= 0 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > count:
                    final = s[l : r + 1]
                    count = r - l + 1
                r += 1
                l -= 1

            

            l = i
            r = i + 1
            while l>= 0 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > count:
                    final = s[l : r + 1]
                    count = r - l + 1
                r += 1
                l -= 1
        return final
