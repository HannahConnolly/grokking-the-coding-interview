# class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next


class Solution:
    def reverse(self, head):
        result = None
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


# next

# curr

# prev
