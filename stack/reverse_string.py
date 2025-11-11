class Solution:
    def reverseString(self, s):

        stack = []
        for chr in s:
            stack.append(chr)

        out = []
        while stack:
            out.append(stack.pop())

        return "".join(out)
