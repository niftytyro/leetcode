# 1 2 3 5 6 7 8

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for idx, val in enumerate(nums):
            if val == target:
                return idx
            if target < val:
                return idx
        return len(nums)


tests = [
    (
        ([1, 3, 5, 6], 5),
        2,
    ),
    (([1, 3, 5, 6], 2), 1),
    (([1, 3, 5, 6], 7), 4),
    (([1, 3, 5, 6], 0), 0),
    (([1], 0), 0),
]
