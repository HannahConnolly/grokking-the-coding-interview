class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_list = []
        vowel = {"a", "e", "i", "o", "u"}

        string_list = list(s)

        for ch in string_list:
            if ch.lower() in vowel:
                print(ch)
                vowel_list.append(ch)
            
        for i, ch in enumerate(string_list):
            if ch.lower() in vowel:
                print(ch)
                string_list[i] = vowel_list.pop()
        
        return "".join(string_list)
