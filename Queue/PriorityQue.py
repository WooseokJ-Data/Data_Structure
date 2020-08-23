class Node:
    def __init__(self, item):
        self.item = item
        self.previous = None
        self.next = None
        
    def get_item(self):
        return self.item
    
    def get_previous(self):
        return self.previous
    
    def get_next(self):
        return self.next
    
    def set_item(self, new_item):
        self.item = new_item
        
    def set_previous(self, previous_item):
        self.previous = previous_item
        
    def set_next(self, next_item):
        self.next = next_item
        
class PriorityQueue:
    
    def __init__(self):
        self.haed = None
    
    def enqueue(self, item):
        current = self.head
        previous = None
        stop = False
        while current !=None and not stop:
            if current.get_item() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        
        new_node = Node(item)
        if previous == None:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            new_node.set_next(current)
            current.set_next(new_node)
            
    def dequeue(self):
        if self.head == None:
            return None
    
        else:
            temp = self.head
            dequeued_item = temp.get_item()
            self.head = self.head.get_next()
            return dequeued_item