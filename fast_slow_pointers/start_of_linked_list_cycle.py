# class Node:
#   def __init__(self, value, next=None):
#     self.val = value
#     self.next = next

class Solution:
    def findCycleStart(self, head):
        def calculate_cycle_len(meeting_node):
            length = 1
            current = meeting_node.next
            while current != meeting_node:
                length += 1
                current = current.next
            return length

        if not head or not head.next:
            return None

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle_len = calculate_cycle_len(slow)
                break
        else:
            return None

        ptr1, ptr2 = head, head
        for _ in range(cycle_len):
            ptr2 = ptr2.next

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1
