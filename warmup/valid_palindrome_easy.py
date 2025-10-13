class Solution:
  def isPalindrome(self, s: str) -> bool:

    s_list = [char.lower() for char in s if char.isalnum()]

    
    start, end = 0, len(s_list) - 1
    while start < end:
      if s_list[start] == s_list[end]:
        start += 1
        end -= 1
      else:
        return False
  
    return True
