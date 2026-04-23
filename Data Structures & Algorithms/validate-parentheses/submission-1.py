class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        values = {")" : "(", "]" : "[", "}" : "{"}
        stack = []
        for i in s:
            if i in values:
                if stack and values[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)


        return not stack 

            