class DoublyLinkedLists():
    def __init__(self):
        self.head= None
        if nodes is not None:
            node=Node(data=nodes.pop(0))
            self.head=node
            for elem in nodes:
                node.next=Node(data=elem)
                node= node.next
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None