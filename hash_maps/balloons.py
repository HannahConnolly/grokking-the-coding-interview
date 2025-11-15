from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        min_count = float('inf')
        
        balloon_dict = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }

        for chr in text:
            balloon_dict[chr] += 1

        balloon_dict['l'] = int(balloon_dict['l'] / 2)
        balloon_dict['o'] = int(balloon_dict['o'] / 2)

        for chr, val in balloon_dict.items():
            if val < min_count:
                min_count = val
        
        print(balloon_dict)

        return min_count

