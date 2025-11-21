from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransom_dict = {}
        magazine_dict = {}

        for char in magazine:
            magazine_dict[char] = magazine_dict.get(char, 0) + 1

        for char in ransomNote:
            ransom_dict[char] = ransom_dict.get(char, 0) + 1

        for key, value in ransom_dict.items():
            if not key in magazine_dict:
                return False
            if value > magazine_dict[key]:
                return False

        return True
