import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z\d]", "", s)

        i = 0
        j = len(s) - 1

        while j - i > 0:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


tests = [
    (
        ("A man, a plan, a canal: Panama",),
        True,
    ),
    (
        ("race a car",),
        False,
    ),
    ((" ",), True),
]
