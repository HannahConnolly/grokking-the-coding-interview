class Solution:

  def search(self, arr, target_sum):
   
    start, end = 0, len(arr) - 1

    while start < end:
      i_sum = arr[start] + arr[end]
      if i_sum == target_sum:
        return [start, end]
      elif i_sum < target_sum:
        start += 1
      else:
        end -= 1

    return [-1, -1]
