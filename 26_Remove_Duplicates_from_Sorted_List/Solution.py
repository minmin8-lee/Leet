class Solution:
    def removeDuplicates(self, nums) -> int:
        place = 1
        for cursor in range(1,len(nums)):
            if nums[cursor] > nums[place-1]:
                nums[place] = nums[cursor]
                place += 1
        return len(nums[:place])

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([0,0,1,3,3,3,4,4,5,5,6,6]))
