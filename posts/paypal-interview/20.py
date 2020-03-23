from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        rightLeftMapping = {
            "]": "[",
            ")": "(",
            "}": "{",
        }
        stack = []

        for v in s:
            if v in set("([{"):
                stack.append(v)
            else:
                if stack:
                    if stack[-1] == rightLeftMapping[v]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        if stack:
            return False
        else:
            return True