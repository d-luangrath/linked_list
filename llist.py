# creates a linked list
from collections import deque
# with "deque" you can access,insert or remove elements from the beginning or end of the list with constant O(n)
# Queue - FIFO
# Stacks - LIFO

# retrieval of elements O(n) bc you travserse through the entire list

# create a class to represent your linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            node.append(node.data)
            node = node.next
        nodes.append("None")
        return " ->".join(nodes)
    
    # traversing the linked list
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # insert a new node at the beginning
    def add_first(self, node):
        node.next = self.head
        self.head = node

    # inserting a new node at the end
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    # inserting between two nodes
    # inserting after an existign node
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        
        raise Exception(f'Node with data {target_node_data} not found')
    
    # inserting before an existing node
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)
        
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f'Node with data {target_node_data} not found')
    
    # remove a node. traverse thru the list until you find the target node, link its prev and next nodes. This is re-linking.
    # you keep track of the prev node as you traverse the list
    def remove_node(self, target_node_data):
        if self.head = None:
            raise Exception("List is empty")
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node








# create a class to represent each node of a linked list
class node:
    def __inti__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data