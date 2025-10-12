class Solution:
  def checkIfPangram(self, sentence):
    alphabet = {ch.lower() for ch in sentence if ch.isalpha()}
    return len(alphabet) == 26  # Check if all 26 letters are present
