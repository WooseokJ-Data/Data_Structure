#Queue with Python
class Queue_Plist:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)
    
    def size(self):
        return len(self.items)

# Queue with Circular List
class Queue:
    def __init__(self):
        '''Queue rear'''
        self.head = None 
    
    def is_empty(self):
        return self.head == None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            
            new_node.set_next(new_node)
            self.head = new_node
        else:
            new_node.set_next(self.head.get_next())
            self.head.set_next(new_node)
            self.head = new_node
            
    def dequeue(self):
        if self.is_empty():
            return None
        
        else:
            temp = self.head.get_next()
            item = temp.get_item()
            if temp = temp.get_next():
                self.head = None
            else:
                self.head.set_next(temp.get_next())
            
            return item
        
    
    def size(self):
        count = 0
        if self.is_empty():
            return count
        current = self.head.get_next()
        while current != self.head:
            current = current.get_next()
            count += 1
            
        return count
        