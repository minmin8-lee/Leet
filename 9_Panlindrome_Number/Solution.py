class Solution:
    # F/Up : Could you solve it without converting the integer to a string?
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = 1
        in_order = []
        reverse_order = []
        x = abs(x)

        while x % 10**n < x:
            target = int((x % 10**n - x % 10**(n-1)) / 10**(n-1))
            reverse_order.append(target)
            in_order.insert(0, target)
            n += 1
        reverse_order.append(int((x % 10**n - x % 10**(n-1)) / 10**(n-1)))
        in_order.insert(0, int((x % 10**n - x % 10**(n-1)) / 10**(n-1)))

        for i in range(len(in_order)):
            if in_order[i] == reverse_order[i]:
                continue
            else:
                return False
        return True

    def isPalindrome_string(self, x:int) -> bool:
        if x < 0 :
            return False
        x = str(x)
        return x == x[::-1]


if __name__ == '__main__':
    s = Solution().isPalindrome(5335)
    print(s)
    print(Solution().isPalindrome_string(535))
