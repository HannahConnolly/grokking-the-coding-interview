class Solution:
    def numGoodPairs(self, nums):
        pairs = 0

        for num in nums:

            if num in value_map:
                value_map[num] += 1
                pairs += value_map[num] - 1

            else:
                value_map[num] = 1

        return pairs
