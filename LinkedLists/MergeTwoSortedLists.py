# LEETCODE 21
# You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
 
# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

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
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        
        curr.next = list1 if list1 else list2
        return dummy.next

if __name__ == "__main__":
    ll = LinkedList()
    list1 = [1,2,3,4,6]
    ll.insert_values(list1)
    newhead1 = ll.head

    ll2 = LinkedList()
    list2 = [2,4,5,6,8,9]
    ll2.insert_values(list2)
    newhead2 = ll2.head
    sol = Solution()
    mergedList = sol.mergeTwoLists(newhead1, newhead2)
    
    # create new linked list for merged list print new merged list
    curr = mergedList

    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")