class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for v in s:
            if v in "([{":
                stack.append(v)
            else:
                if stack == []:
                    return False
                else:
                    if stack[-1] == "(" and v == ")":
                        stack.pop()
                    elif stack[-1] == "[" and v == "]":
                        stack.pop()
                    elif stack[-1] == "{" and v == "}":
                        stack.pop()
                    else:
                        return False

        return stack == []