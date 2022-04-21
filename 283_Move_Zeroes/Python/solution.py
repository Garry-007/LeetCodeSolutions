class Solution(object):
    def swap(self, nums, x, y):
        temp = nums[x]
        nums[x] = nums[y]
        nums[y] = temp

    def moveZeroes(self, nums):
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                self.swap(nums, j, i)
                j += 1
