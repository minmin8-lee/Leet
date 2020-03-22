class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CODE = {"(": 1, "{": 1, "[": 1,
                ")": -1, "}": -1, "]": -1}
        SET = {")": "(", "}": "{", "]": "["}

        for e in s:
            if CODE[e] > 0:
                stack.append(e)
            else:
                try:
                    if stack.pop() == SET[e]:
                        continue
                    else:
                        return False
                except:
                    return False
        if not stack:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution().isValid("[[[[[{}]]]]]({})[]")
    print(s)
