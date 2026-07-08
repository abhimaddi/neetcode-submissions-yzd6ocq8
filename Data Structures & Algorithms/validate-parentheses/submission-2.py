class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeMap = {")" : "(", "]" : "[", "}":"{"}
        for para in s:
            if para in closeMap:
                if stack and stack[-1] == closeMap[para]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(para)
        if stack:
            return False
        else:
            return True