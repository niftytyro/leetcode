# 1 2 3

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] >= target else 1
        mid = len(nums) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            return mid + self.searchInsert(nums[mid:], target)
        return self.searchInsert(nums[:mid], target)


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
