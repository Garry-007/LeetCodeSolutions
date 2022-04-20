class Solution(object):
    def reverse(self, nums, i=0, j=None):
        # reverse the entire array by default
        j = len(nums) - 1 if j is None else j
        left = i
        right = j
        while left < right:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            left += 1
            right -= 1

    def rotate(self, nums, k):
        if k == 0:
            return
        real_k = k % len(nums)
        # reverse k elements from the end
        self.reverse(nums, len(nums) - real_k, len(nums) - 1)
        # reverse the remaining elements
        self.reverse(nums, 0, len(nums) - real_k - 1)
        # reverse the whole list to get the result
        self.reverse(nums)

    # Simple python way
    # def rotate(self, nums, k):
    #     real_k = k % len(nums)
    #     if real_k != 0:
    #         nums[:] = nums[-real_k:] + nums[:len(nums) - real_k]

    # Too slow
    # def rotate(self, nums, k):
    #     real_k = k % len(nums)
    #     for i in range(0, real_k):
    #         nums.insert(0, nums.pop())
