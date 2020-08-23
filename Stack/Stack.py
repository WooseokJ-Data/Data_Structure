#STACK with Python List

class Stack_with_Plist:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.appent(item)
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            self.items[len(self.items)-1]
            
    def size(self):
        return len(self.items)
    
#Stack with simply linked list

#단순 연결 리스트로 구현한 스택
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
    
    def get_next(self):
        return self.next
 
    def get_item(self):
        return self.item
    
    def set_item(self, new_item):
        self.item = new_item
        
    def set_next(self, new_next):
        self.next = new_next

class Stack:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def push(self,item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            pop_item = self.head.item
            self.head = self.head.get_next()
            return pop_item
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.get_item()
    
    def size(self):
        current = self.head
        count =0
        while current != None:
            count +=1
            current = current.get_next()
        return count
    
    