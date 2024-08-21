class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def insertAtTail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtHead(data)
            return

        possition = 0
        curr_node = self.head
        while curr_node and possition + 1 != index:
            possition += 1
            curr_node = curr_node.next

        if not curr_node:
            raise Exception('Index not present')

        new_node = Node(data)
        new_node.next = curr_node.next
        curr_node.next = new_node

    def visualize(self):
        size = 0
        data_list = []

        if self.head:
            curr_node = self.head
            while (curr_node):
                size += 1
                data_list.append(curr_node.data)
                curr_node = curr_node.next

        print(f'size: {size}')
        print(f'data: {' -> '.join(map(str, data_list))}')


llist = LinkList()
llist.insertAtHead(1)
llist.insertAtHead(2)
llist.insertAtTail(7)
llist.insertAtTail(5)
llist.visualize()

llist.insertAtIndex(11, 2)
llist.insertAtIndex(13, 3)
llist.visualize()
