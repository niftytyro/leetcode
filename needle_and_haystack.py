# Find the Index of the First Occurrence in a String


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pos = -1

        for idx in range(len(haystack)):
            matched = True
            for needle_idx in range(len(needle)):
                if (
                    len(haystack) <= idx + needle_idx
                    or needle[needle_idx] is not haystack[idx + needle_idx]
                ):
                    matched = False
                    break

            if matched:
                pos = idx
                break

        return pos


tests = [
    (
        ("sadbutsad", "sad"),
        0,
    ),
    (
        ("leetcode", "leeto"),
        -1,
    ),
]
