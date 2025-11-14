from collections import defaultdict


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        maxUnique = -1

        freq_chart = {}

        for num in A:
            freq_chart[num] = freq_chart.get(num, 0) + 1

        for num, freq in freq_chart.items():
            if num > maxUnique and freq == 1:
                maxUnique = num

        return maxUnique
