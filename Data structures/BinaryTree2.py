class Node:
    def __init__(self,data):
        self.data= data
        self.left=None
        self.right=None

    
class BinaryTree:
    def __init__(self):
        self.root=None

    def add_Node(self, node):
        if  self.root==None:
            self.root=node
        else:
            aux = self.root
            father = None
            while aux != None:
                father = aux
                if (node.data>= aux.data):
                   aux= aux.right
                else:
                    aux=aux.left
            if (node.data >= father.data):
                father.right=node
            else:
                father.left=node
    
    def preorder(self, node):
        if node != None:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
         if node!=None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)


    def postorder(self, node):        
        if node!=None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)

    def getRoot(self):
        return self.root

if __name__== "__main__":

    bt=BinaryTree()
    bt.add_Node(Node(12))
    bt.add_Node(Node(10))
    bt.add_Node(Node(14))
    bt.preorder(bt.getRoot())
    bt.inorder(bt.getRoot())
    bt.postorder(bt.getRoot())