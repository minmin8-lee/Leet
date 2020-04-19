class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for i, n in enumerate(nums):
            if n == target or n > target:
                return i
        return len(nums)

if __name__ == '__main__':
    s = Solution().searchInsert([-1,0,5,6],2)
    print(s)
