class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

if __name__ == '__main__':
    s = Solution().removeElement([3,3,3,3,1,1,1,1],3)
    print(s)
