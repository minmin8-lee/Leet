class Solution:
    def removeElement(self, nums, val: int) -> int:
        place = 0
        while True:
            swapped = False
            if place >= len(nums):
                return len(nums[:place])

            if nums[place] == val:
                for i in range(place,len(nums)):
                    if nums[i] != val:
                        nums[place] = nums[i]
                        nums[i] = val
                        swapped = True
                        break
                if not swapped:
                    return len(nums[:place])
            place += 1

if __name__ == '__main__':
    s = Solution().removeElement([3,3,3,3,3,3,3,1],3)
    print(s)
