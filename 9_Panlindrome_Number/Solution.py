class Solution:
    # F/Up : Could you solve it without converting the integer to a string?
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        in_order = []
        reverse_order = []

        while x > 0:
            target = x % 10
            reverse_order.append(target)
            in_order.insert(0, target)
            x //= 10

        return reverse_order == in_order

    def isPalindrome_string(self, x:int) -> bool:
        if x < 0 :
            return False
        x = str(x)
        return x == x[::-1]


if __name__ == '__main__':
    s = Solution().isPalindrome(5335)
    print(s)
    print(Solution().isPalindrome_string(535))
