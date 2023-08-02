"""
This is a simple problem - finding the min and max with a twist.
In this, we need to find a pair of array values such that their difference is the highest among all other possible values and the latter value is greater than the first.

One simple algorithm is this.
Loop through the array.
    Take the rest of array (after this value).
    Find the maximum value in the remaining array.
    See if the difference between this and the first value is higher.

1) Correctness
2) Ease of implementation
3) Efficiency: O(n^2)

One tweak to improve performance:
when looping, check for the difference between this number and the largest value in the array itself. Only, if this is larger than currently, largest difference, there is a point of looping through the remaining array. Can skip out quite a few numbers this way.


Okay, found a better solution.
Keep 2 pointers. Left and right.
Left = 0
Right = 1
While true:
    if left < right:
        max_profit = max(right - left, oldProfit)
    else:
        left = right
    right += 1 
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = 1

        while right < len(prices):
            current_profit = prices[right] - prices[left]
            max_profit = max(current_profit, max_profit)
            if prices[right] < prices[left]:
                left = right

            right += 1

        return max_profit


tests = [
    (([7, 1, 5, 3, 6, 4],), 5),
    (([7, 6, 4, 3, 1],), 0),
]
