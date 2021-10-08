from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        offset = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 0
                offset -= 1
            elif i - offset:
                nums[offset] = nums[i]
                nums[i] = 0
            offset += 1
        return offset


tests = [
    (
        ([3, 2, 2, 3], 3),
        2,
    ),
    (
        ([0, 1, 2, 2, 3, 0, 4, 2], 2),
        5,
    ),
    (
        ([0, 1, 2, 2, 3, 0, 4, 2], 2),
        5,
    ),
]
