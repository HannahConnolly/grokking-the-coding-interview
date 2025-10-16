class Solution:
    def moveElements(self, arr):
        if len(arr) < 2:
            return len(arr)

        non_duplicate, new_non_duplicate, unique = 0, 1, 1

        while new_non_duplicate < len(arr):
            # duplicate number found, keep searching for new number
            if arr[non_duplicate] == arr[new_non_duplicate]:
                new_non_duplicate += 1

            # non duplicate found, move to sorted front
            else:
                non_duplicate += 1
                arr[non_duplicate] = arr[new_non_duplicate]
                new_non_duplicate += 1
                unique += 1

        print(arr)
        return unique
