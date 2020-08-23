class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None

    def add_last(self, item):
           
        new_node=Node(item)        
        if self.is_empty():
            self.head = new_node
                    
        else:
            start_node = self.head
            while start_node.next:
                start_node=start_node.next
                       
            start_node.next=new_node
        

    def add_first(self, item):
        ## Completed Function - Do not remove
        # Add a value in the begin of the list
        new_node = Node(item)
        
        if not self.is_empty():
            new_node.next = self.head

        self.head = new_node
        
                
    def delete_last(self):
        # Delete a value in the end of the list
        start_node=self.head
        previous_node=start_node
        if self.is_empty():
            print('The list is empty')
            return
        
        while start_node.next:
            previous_node=start_node
            start_node=start_node.next
        
        if previous_node.next==None:
            self.head=None
        
        previous_node.next=None
               
    
    def delete_first(self):
        # Delete a value in the begin of the list

        start_node=self.head
        
        self.head=start_node.next
        
    def pop_first(self):
        
        start_node = self.head
        
        return start_node.value
    
    def pop_last(self):
        
        start_node = self.head
        while start_node.next:
            start_node = start_node.next
            
        return start_node.value

        
    def display(self):
        
        if self.is_empty():
            print("linked list is empty !!")
            
        else:
            values = []

            start_node = self.head
            while start_node:
                values.append(start_node.value)
                start_node = start_node.next

            print("linked list values> ", ' -> '.join(map(str,values)))
            
        
    
    def get_length(self):
        # Get length of the list
        start_node = self.head
        i=0
        while start_node:
            start_node = start_node.next
            i+=1
        return i
        

    def is_empty(self):
        # Check if the list is empty
        if self.head == None:
            return True
        pass
    
def main():
    
    linked_list = LinkedList()
    
    linked_list.add_last(3)
    linked_list.add_last(7) 
    linked_list.add_last(4) 
    linked_list.display() # Expected Result: linked list values>  3 -> 7 -> 4
    
    linked_list.add_first(1)
    linked_list.add_first(2)
    linked_list.display() # Expected Result: linked list values>  2 -> 1 -> 3 -> 7 -> 4


    print('pop_first is:',linked_list.pop_first())
    print('pop last is', linked_list.pop_last())
    linked_list.delete_first()
    linked_list.display()
    linked_list.delete_last()
    linked_list.display() # Expected Result: linked list values>  1 -> 100 -> 3 -> 7
    
    linked_list.delete_first()
    linked_list.delete_last()
    linked_list.delete_first()
    linked_list.display() # Expected Result: linked list values>  3
    
    linked_list.delete_last()
    linked_list.display() # Expected Result: linked list is empty !!
    
        
main()
