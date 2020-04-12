class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        i = 0 
        while i < (len(haystack) - len(needle) + 1):
            if needle == haystack[i: i + len(needle)]:
                return i 
            else:
                i = i + 1
        return -1
