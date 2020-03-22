class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        score = 0
        CODE = {"(": 1, "{": 1, "[": 1,
                ")": -1, "}": -1, "]": -1}
        SET = {")": "(", "}": "{", "]": "["}

        for e in s:
            if CODE[e] == 1:
                score += CODE[e]
                stack.append(e)
            elif CODE[e] < 0:
                score += CODE[e]
                if score < 0:
                    return False
                elif stack[-1] == SET[e]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        if score == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution().isValid("[]")
    print(s)
