class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_map = {}

        for ch in s:
            my_map[ch] = my_map.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if my_map[ch] == 1:
                return i

        return -1
