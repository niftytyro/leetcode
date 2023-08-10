from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0

        while j < n and i < m + n:
            if i >= m:
                nums1[i] = nums2[j]
                i += 1
                j += 1
                continue

            # Get to the point, where nums2[j] has to be inserted
            while nums1[i] < nums2[j] and i < m:
                i += 1

            print(i)

            # Insert nums2[j]
            for x in range(m, i, -1):
                nums1[x] = nums1[x - 1]
            nums1[i] = nums2[j]
            i += 1
            j += 1
            m += 1

        print(nums1)


tests = [
    (([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), None),
    (([1], 1, [], 0), None),
    (([0], 0, [1], 1), None),
]
