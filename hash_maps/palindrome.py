class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        my_map = {}

        for char in s:
            my_map[char] = my_map.get(char, 0) + 1

        has_odd = False

        for value in my_map.values():
            if value % 2 == 0:
                length += value
            else:
                length += value - 1
                has_odd = True

        if has_odd:
            length += 1

        return length
