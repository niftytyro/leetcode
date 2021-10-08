from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 1
        end = 0
        while length < len(nums):
            if nums[length] == nums[end]:
                nums[length] = 0
                end -= 1
            elif length - end > 1:
                nums[end + 1] = nums[length]
                nums[length] = 0
            end += 1
            length += 1
        return end + 1


tests = [
    (
        ([1, 1, 2],),
        2,
    ),
    (
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],),
        5,
    ),
]
