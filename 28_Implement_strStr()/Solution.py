class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) < 1 or haystack == needle:
            return 0

        for i in range(len(haystack)):
            go_home = True
            if haystack[i] == needle[0]:
                if len(haystack[i:]) >= len(needle):
                    for n in range(1, len(needle)):
                        if haystack[i+n] != needle[n]:
                            go_home = False
                    if go_home:
                        return i
                else:
                    return -1
        return -1


if __name__ == '__main__':
    s = Solution()
    ans = s.strStr("aaaaaaaaaaaaaaaa", "aaa")
    print(ans)
