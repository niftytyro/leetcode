"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Simple problem.

Brute force method is to loop through each element and loop through the rest to find a duplicate.


More efficient method:
Sort the array.
Loop through the array, checking current and next number. If not same, keep going.

Time Complexity: O(n x log n)
Sorting takes O(n x log n)
Looping takes O(n)
"""


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        has_duplicate = False

        for i in range(len(nums) - 1):
            j = i + 1
            if nums[i] == nums[j]:
                has_duplicate = True
                break

        return has_duplicate


tests = [
    (([1, 2, 3, 1],), True),
    (([1, 2, 3, 4],), False),
    (([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],), True),
]
