class Solution:
    def isValid(self, s: str) -> bool:

        openclose_map = {"(" : ")","[" : "]", "{": "}"}
        stack = []

        for c in s:
            if c in openclose_map.keys():
                stack.append(c)

            elif c in openclose_map.values():
                if not stack or openclose_map[stack.pop()] != c:
                    return False

        return not stack
