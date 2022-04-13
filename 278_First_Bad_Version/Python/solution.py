# isBadVersion() comes from an external API

class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        lowest_bad = n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                if mid < lowest_bad:
                    lowest_bad = mid
                right = mid - 1
            elif not isBadVersion(mid):
                left = mid + 1
        return lowest_bad
