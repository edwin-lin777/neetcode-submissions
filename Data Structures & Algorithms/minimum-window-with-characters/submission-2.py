class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        have = 0
        need_count = len(need)

        left = 0
        best_len = float("inf")
        best = ""

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_count:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best = s[left:right + 1]

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return best
