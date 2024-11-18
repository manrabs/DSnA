# LEETCODE 83 - Sol1 class
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

# LEETCODE 206 - Reverse Linked List - Sol2 class
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []
# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_values(self, data_list):
        # this function creates a linked list out of the provided list by inserting each value in list to the end of the linked list
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def insert_at_end(self, data):
        # if list is empty, add new value to list. note that the next value is None (i.e. there is no next value)
        if self.head is None:
            self.head = ListNode(data, None)
            return

        itr = self.head

        # keep looping till you get to last element. i.e, element whose next element is null
        while itr.next:
            itr = itr.next
        # once at end, add the new element as the next value whose own next value is null
        itr.next = ListNode(data, None)
class Sol1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

class Sol2:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
    
if __name__ == "__main__":
    ll = LinkedList()
    head = [1,2,2,2,3,4,5,5,6,7,8,8,9,10]
    ll.insert_values(head)

    sol = Sol1()
    sol2 = Sol2()
    
    updated_head = sol.deleteDuplicates(ll.head)
    # Traverse and print the updated linked list

    curr = updated_head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

    updated_head2 = sol2.reverseList(ll.head)
    # Traverse and print the updated linked list
    curr2 = updated_head2
    while curr2:
        print(curr2.val, end=" -> ")
        curr2 = curr2.next
    print("None")