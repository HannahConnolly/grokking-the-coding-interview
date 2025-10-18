class Solution:
    def searchTriplets(self, arr):
        triplets = []
        arr.sort()
        i = 0

        while i < len(arr) - 2:
            num = arr[i]
            
            if i > 0 and arr[i] == arr[i - 1]:
                i += 1
                continue

            left, right = i + 1, len(arr) - 1
            while left < right:
                s = num + arr[left] + arr[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    triplets.append([num, arr[left], arr[right]])

                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

            i += 1

        return triplets
