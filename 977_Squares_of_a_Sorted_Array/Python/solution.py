class Solution(object):
    def sortedSquares(self, nums):
        output_array = []
        left = 0
        right = len(nums) - 1
        while left <= right:
            l_sq = nums[left] ** 2
            r_sq = nums[right] ** 2
            if l_sq > r_sq:
                output_array.append(l_sq)
                left += 1
            else:
                output_array.append(r_sq)
                right -= 1
        return output_array[::-1]
