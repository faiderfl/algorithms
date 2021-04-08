#Ordered collection of objects. 
#Lists use a contiguous memory block to store references to their data, linked lists store references as part of their own elements.

from collections import deque

dq=deque('abcd')
dq.append('e')
dq.pop()
dq.appendleft('e')
first= dq.popleft()
last=dq.pop()

print(first, last)


#Own Linked List

class LinkedList():
    def __init__(self, nodes=None):
        self.head=None
        if nodes is not None:
            node=Node(data=nodes.pop(0))
            self.head=node
            for elem in nodes:
                node.next=Node(data=elem)
                node= node.next
    
    def __repr__(self):
        node=self.head
        nodes=[]

        while node is not None:
            nodes.append(node.data)
            node = node.next

        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node=self.head
        while node is not None:
            yield node
            node=node.next
    
    def add_first(self, node):
        node.next=self.head
        self.head=node
        
    def add_last(self, node):
        if self.head is None:
            self.head=node
            return
        for current_node in self:
            pass
        current_node.next=node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('Empty List')
        
        for node in self:
            if node.data== target_node_data:
                new_node.next = node.next
                node.next= new_node
                return
        raise Exception(f"Node with data '%s' not found" %target_node)

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

        raise Exception("Node with data '%s' not found" % target_node_data)
        
    def remove_node(self, target_node_data):
        if self.head is None:
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

        raise Exception("Node with data '%s' not found" % target_node_data)

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

    def __repr__(self):
        return self.data

linkedList = LinkedList()
linkedList2= LinkedList(['1','2'])

first_node= Node('a')
linkedList.head=first_node
linkedList2.add_first(first_node)
linkedList2.add_last(Node('z'))
linkedList2.add_after('a',Node('y'))

for node in linkedList2:
    print(node)