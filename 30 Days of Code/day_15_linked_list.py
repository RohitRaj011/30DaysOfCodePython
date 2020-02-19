class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        new_node = Node(data)  # creating node with user-data
        # if head is empty, new node is head
        if head == None:
            head = new_node
        # else iterate to the end and append the new node
        else:
            current = head
            while current.next != None:
                current = current.next
            current.next = new_node
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
