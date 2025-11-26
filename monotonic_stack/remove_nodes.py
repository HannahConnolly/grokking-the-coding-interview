# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNodes(self, head):
        stack = []
        cur = head

        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()
            if stack:
                stack[-1].next = cur
            stack.append(cur)
            cur = cur.next

        return stack[0] if stack else None
