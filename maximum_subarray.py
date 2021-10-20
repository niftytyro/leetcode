from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        maxSum = sum
        for i in nums[1:]:
            if i + sum < i:
                sum = i
            else:
                sum += i
            maxSum = max(maxSum, sum)
        return maxSum


tests = [
    (
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4],),
        6,
    ),
    (
        ([1],),
        1,
    ),
    (
        ([5, 4, -1, 7, 8],),
        23,
    ),
]
