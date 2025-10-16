class Solution:
    def makeSquares(self, arr):
        squared = []

        if len(arr) == 0:
            return arr

        if arr[-1] < 0:
            return [x * x for x in arr[::-1]]
        if arr[0] >= 0:
            return [x * x for x in arr]

        positive, negative = len(arr) - 1, len(arr) - 2

        # find first positive number:
        for i, num in enumerate(arr):
            print(i, num)
            if num >= 0:
                positive = i
                negative = i - 1
                break

        while positive < len(arr) and negative >= 0:
            if (arr[positive] ** 2) <= (arr[negative] ** 2):
                squared.append(arr[positive] ** 2)
                positive += 1
            else:
                print("here ", negative)
                squared.append(arr[negative] ** 2)
                negative -= 1

        while positive < len(arr):
            squared.append(arr[positive] ** 2)
            positive += 1

        while negative >= 0:
            squared.append(arr[negative] ** 2)
            negative -= 1

        return squared
