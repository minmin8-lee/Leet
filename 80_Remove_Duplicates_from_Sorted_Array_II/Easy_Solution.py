class Solution:
    def removeDuplicates(self, nums) -> int:
        target = 0
        flag = 0
        while target < len(nums) - 1:
            if nums[target] == nums[target + 1]:
                flag += 1
            else:
                flag = 0

            if flag > 1:
                del (nums[target])
            else:
                target = target + 1

        return len(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([0,0,1,3,3,3,4,4,5,5,6,6]))
