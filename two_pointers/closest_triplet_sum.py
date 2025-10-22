import math

class Solution:
    def searchTriplet(self, arr, target_sum):
        arr.sort()
        closest_sum = float('inf')

        for i in range(len(arr) - 2):
            left, right = i + 1, len(arr) - 1

            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]

                if (abs(target_sum - current_sum) < abs(target_sum - closest_sum)) or \
                   (abs(target_sum - current_sum) == abs(target_sum - closest_sum) and current_sum < closest_sum):
                    closest_sum = current_sum

                if current_sum < target_sum:
                    left += 1
                elif current_sum > target_sum:
                    right -= 1
                else:
                    return closest_sum

        return closest_sum
