class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp = {")" : "(", "]" : "[", "}" : "{"}
        for i in s:
            if i in mapp:
                if stack and stack[-1] == mapp[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        return True