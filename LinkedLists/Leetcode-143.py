# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Example 1 :
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2: 
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Constraints:
# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000

from optional import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # finds middle of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next # this marks beginning of 'second half' of the list
        slow.next = None # this splits the list into two by pointing the first item in the 'second half' of list to null, thus breaking the link. this allows me to reverse the 'second half' of the list
        prev = None
        
        # reverses second half of list
        while second_half:
            tmp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = tmp
        
        # merges two halfs of list
        first_half, second_half = head, prev
        while second_half:
            tmp1, tmp2 = first_half.next, second_half.next
            first_half.next = second_half
            # this line inserts the second node in between the first and first.next, and is the main merging operation here
            second_half.next = tmp1
            first_half, second_half = tmp1, tmp2