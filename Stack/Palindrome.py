import Stack    
    
# Palindrome1
def palindrome1(string):
    s = Stack()
    palindrome = True
    if len(string)%2 == 0:
        for i in string[:len(string)//2]:
            s.push(i)
        for j in string[len(string)//2:]:
            temp = s.pop()
            if j != temp:
                palindrome = False
                break
    else:
        for i in string[:len(string)//2]:
            s.push(i)
        for j in string[len(string)//2+1:]:
            temp = s.pop()
            if j != temp:
                palindrome = False
                break
    return palindrome

# Palindrome2
def palindrome2(string):
    s = Stack()
    reversed_string = ''
    for i in string:
        s.push(i)
    while not s.is_empty():
        reversed_string = reversed_string + s.pop()
    
    if string == reversed_string:
        return True
    else:
        return False
