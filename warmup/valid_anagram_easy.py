class Solution:
  def isAnagram(self, s, t):
    
    if len(s) != len(t):
      return False
    
    letter_map = {}

    for ch in s:
      letter_map[ch] = letter_map.get(ch, 0) + 1

    for ch in t:
      if letter_map.get(ch, 0) == 0:
        return False
      letter_map[ch] -= 1

    return True
