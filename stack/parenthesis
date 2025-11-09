class Solution:
    def isValid(self, s):
        
        stack = []
        closing_paren = "})]"

        paren_pair = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for ch in s:
            if ch in closing_paren:
                if paren_pair[ch] != stack.pop():
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0
