#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  def findMiddle(self, head):
    
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast:
        if fast.next:
            fast = fast.next.next
        else:
            fast = None
        slow = slow.next

    return slow
