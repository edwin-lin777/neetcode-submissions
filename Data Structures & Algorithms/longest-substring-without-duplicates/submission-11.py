class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        left = 0;
        final = 0;
        for r in range(len(s)):
            while s[r] in mySet:
                mySet.remove(s[left]);
                left += 1;
                
            mySet.add(s[r])
            final = max(final, len(mySet))
           
            

        return final;