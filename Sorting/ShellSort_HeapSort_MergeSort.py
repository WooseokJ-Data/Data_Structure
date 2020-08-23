def shell_sort(items):
    h = len(items)//2
    while h>=1:
        for i in range(h, len(items)):
            
            j = i
            
            while j>=h and items[j] <items[j-h] :
                
                items[j] , items[j-h] = items[j-h], items[j]
                j -= h
                
        print('{}-Sorting Result'.format(h), items)
        h = h//2
        
"""        
items = [39,23,15,47,11,56,61,16,12,19,21,41]
print('Before Sorted: ',end='')
print(items)
shell_sort(items)
print('After Sorted: ',end='')
print(items)
"""

def downheap(i, size, items):
    while 2*i +1 <=size:
        k = 2*i +1
        if k<size-1 and items[k] <items[k+1]:
            k+= 1
        if items[i] >= items[k]:
            break
        items[i], items[k] = items[k], items[i]
        i = k
        
def heapify(items):
    hsize = len(items)
    for i in range(hsize//2-1,-1,-1):
        downheap(i,hsize)

def heap_sort(items):
    N = len(items)
    for i in range(N):
        items[0], items[N-1] = items[N-1], items[0]
        downheap(0, N-2)
        N-=1

def merge(items, temp, low, mid , high):
    i = low
    j = mid +1
    for k in range(low,high+1):
        if i>mid:
            temp[k] = items[j]
            j+=1
        elif j>high:
            temp[k] = items[i]
            i+=1
        elif items[j] < items[i]:
            temp[k] = items[j]
            j+=1
        else:
            temp[k] = items[i]
            i +=1
    for k in range(low,high+1):
        items[k] = temp[k]
    
def merge_sort(items,temp,low,high):
    if high<=low:
        return None
    mid = low+(high - low)//2
    merge_sort(items, temp,low,mid)
    merge_sort(items, temp, mid+1, high)
    merge(items, temp, low, mid, high)