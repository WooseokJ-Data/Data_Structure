def selection_sort(items):
    for i in range(len(items)):
        minimum = i
        for j in range(i, len(items)):
            
            if items[minimum] > items[j]:
                minimum = j
        
        items[i], items[minimum] = items[minimum], items[i]
    
    return items

def selection_sort_2(items):
    for i in range(len(items)):

        for j in range(i, len(items)):
            
            if items[i] > items[j]:
                 items[i], items[j] = items[j], items[i]
       
    
    return items

def insertion_sort(items):
    
    for i in range(1,len(items)):
        
        for j in range(i,0,-1):
            
            if items[j-1] > items[j]:
                items[j], items[j-1] = items[j-1], items[j]
                
    return items