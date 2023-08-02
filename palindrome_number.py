class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed = str(x)[::-1]
        return reversed == str(x)


tests = [
    (
        (121,),
        True,
    ),
    (
        (-121,),
        False,
    ),
    (
        (10,),
        False,
    ),
]
