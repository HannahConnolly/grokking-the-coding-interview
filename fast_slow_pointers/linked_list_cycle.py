# class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next


class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        print("got here")
        slow, fast = head, head.next

        while fast != None and fast.next != None:
            if fast.val == slow.val:
                return True

            slow = slow.next
            fast = fast.next.next

        return False
