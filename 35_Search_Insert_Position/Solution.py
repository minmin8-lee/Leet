class Solution:
    def searchInsert(self, nums, target: int) -> int:
        low_bound = 0
        upp_bound = len(nums) - 1

        if target <= nums[low_bound]:
            return 0
        elif target >= nums[upp_bound]:
            return len(nums)
        else:
            return self.search(nums, target)

    def search(self, nums, target):
        #  step 1. set initial values
        low_bound = 0
        upp_bound = len(nums) - 1
        median = low_bound + int((upp_bound - low_bound) / 2)

        #  step 2. loop while lower < upper
        while low_bound < upp_bound:
            median = low_bound + int((upp_bound - low_bound) / 2)

            if nums[median] < target:
                low_bound = median + 1
            elif nums[median] > target:
                upp_bound = median - 1
            else:
                return median

        print("not found")
        return median

if __name__ == '__main__':
    s = Solution().searchInsert([1,2,5,6],3)
    print(s)
