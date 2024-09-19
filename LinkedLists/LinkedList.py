class Node: #this class represents individual elements in the linked list
    def __init__(self, data=None, next=None):
        self.data = data #actual element, can contain integers, stringss, complex objects etc.
        self.next = next #pointer to next element

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        # gets length of entire linked list by beginning at the top (head) of the linked list
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        # if list is empty, add new value to list. note that the next value is None (i.e. there is no next value)
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        # keep looping till you get to last element. i.e, element whose next element is null
        while itr.next:
            itr = itr.next
        # once at end, add the new element as the next value whose own next value is null
        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        # first check that provided index is within the bounds of the linked list
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        # remove first element (i.e. the head) by assigning the next element as the first
        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        # this function creates a linked list out of the provided list by inserting each value in list to the end of the linked list
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next
    
    def remove_value(self, data_to_remove):
        if self.head is None:
            return
        
        if self.head.data == data_to_remove:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data_to_remove:
                itr.next = itr.next.next
                break
            itr = itr.next
        print(str(data_to_remove) + " got removed")
        
    def reverse_list(self):
        prev, curr = None, self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.reverse_list()
    # ll.print()
    # ll.remove_value("mango")
    # ll.print()