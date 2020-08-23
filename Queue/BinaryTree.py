import Queue

class tree_node:
    
    def __init__(self, item, left_child = None, right_child = None):
        self.key =item
        self.left = left_child
        self.right = right_child
        
    def get_key(self):
        return self.key
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def set_key(self, new_item):
        self.key = new_item
    
    def set_right(self,new_right):
        self.right = new_right
    
    def set_left(self, new_left):
        self.left = new_left
        

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def preorder(self, node):
        if node != None:
            print(str(node.get_key()),' ',end='')
            if node.get_left():
                self.preorder(self, node.get_left())
            if node.get_right():
                self.preorder(self, node.get_rigt())
    
    def inorder(self,node):
        if node != None:
            if node.get_left():
                self.inorder(node.get_left())
            print(str(node.get_key()),' ',end='')
            if node.get_right():
                self.inorder(node.get_right())
    
    def postorder(self,node):
        if node != None:
            if self.get_left():
                self.postorder(node.get_left())
            if self.get_right():
                self.postorder(node.get_right())
            print(str(node.get_key()),' ',end ='')
    
    def leverorder(self, root):
        q = Queue()
        q.enqueue(root)
        while not q.is_empty():
            node = q.dequeue
            print(str(node.get_key()),' ',end='')
            if node.get_left():
                q.enqueue(node.get_left())
            if node.qet_right():
                q.enqueue(node.get_right())