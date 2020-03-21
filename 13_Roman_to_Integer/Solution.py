class Solution:
    # With Validation ! 
    def romanToInt(self, s: str) -> int:
        TABLE = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
                 "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        POINT_TABLE = {"I": 1, "X": 1, "C": 1, "V": -1, "L": -1, "D": -1, "M": 0}

        careful = False
        result = []
        stack = []

        for c in s:
            if careful:
                before = stack.pop()
                new_c = before + c
                try:
                    result.append(TABLE[new_c])
                    careful = False
                    continue
                except KeyError:
                    result.append(TABLE[before])
                    careful = False

            if POINT_TABLE[c] > 0:
                stack.append(c)
                careful = True
            else:
                result.append(TABLE[c])

        while len(stack) > 0:
            result.append(TABLE[stack.pop()])
            
        gt = result[0]
        print(result)
        for i in range(len(result)-1):
            if result[i] < result[i+1]:
                print("invalid roman")
                return -1
            else:
                gt += result[i+1]
            i += 1
        return gt


if __name__ == '__main__':
    s = Solution().romanToInt("MMMCMIV")
    print(s)
