class Solution:
  def numGoodPairs(self, nums):
    pairCount = 0
    # TODO: Write your code here

    # Map of values,
    # key - value
    # value - number of times seen (pairs)
    value_map = {}
    pairs = 0

    for num in nums:

      if num in value_map:
        value_map[num] += 1
        pairs += value_map[num] - 1

      else:
        value_map[num] = 1

    return pairs
