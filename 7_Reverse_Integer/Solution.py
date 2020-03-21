class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2147483648, 2147483647
        n, result = 1, 0
        stack = []
        flag = False

        if x >= 0:
            flag = True
        x = abs(x)

        while x % 10**n < x:
            stack.append(int((x % 10**n - x % 10**(n-1)) / 10**(n-1)))
            n += 1
        stack.append(int((x % 10**n - x % 10**(n-1)) / 10**(n-1)))

        for d in stack:
            result += d * pow(10, n-1)
            n -= 1

        if result > MAX or -result < MIN:
            return 0
        if flag:
            return result
        else:
            return -result

    def reverse_string(self, x:int) -> int:
        MIN, MAX = -2147483648, 2147483647
        flag = False
        if x < 0:
            flag = True
        x = str(abs(x))[::-1]
        x = int(x)

        if x > MAX or x < MIN:
            return 0
        if flag:
            return -x
        else:
            return x


if __name__ == '__main__':
    s = Solution()
    print(s.reverse_string(980))
