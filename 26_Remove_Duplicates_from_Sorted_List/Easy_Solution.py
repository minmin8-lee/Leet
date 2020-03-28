# DEL 사용시 매우 간단하므로 del 금지
class Solution:
    def removeDuplicates(self, nums) -> int:
        target = 0
        while target < len(nums)-1:
            if nums[target] == nums[target+1]:
                del(nums[target])
            else:
                target = target+1
        return len(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,2,3,3,3,4,4,5,6]))
