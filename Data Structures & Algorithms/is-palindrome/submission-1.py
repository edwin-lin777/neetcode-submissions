class Solution:
    def isPalindrome(self, s: str) -> bool:
        myString = "".join(c.lower() for c in s if c.isalnum())
        revers = myString[:: -1]
        return myString == revers
