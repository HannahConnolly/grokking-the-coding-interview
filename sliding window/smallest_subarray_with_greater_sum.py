import sys


class Solution:
    def findMinSubArray(self, s, arr):
        if not arr:
            return 0

        front, back = 0, 0
        window_sum = 0
        min_length = sys.maxsize

        while front < len(arr):
            window_sum += arr[front]
            front += 1

            while window_sum >= s:
                min_length = min(min_length, front - back)
                window_sum -= arr[back]
                back += 1

        return min_length if min_length != sys.maxsize else 0
