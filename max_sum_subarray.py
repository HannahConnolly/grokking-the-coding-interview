class Solution:
    def findMaxSumSubArray(self, k, arr):

        if len(arr) < k:
            return -1

        start, end, cur_sum = 0, 0, 0
        best_sum = arr[start]

        while end < len(arr):
            cur_sum += arr[end]

            if end - start == k:
                cur_sum -= arr[start]
                start += 1

            end += 1

            if cur_sum > best_sum:
                best_sum = cur_sum

        return best_sum
