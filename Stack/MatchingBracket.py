
import Stack

# Checking Matching Bracket
def is_balanced(string):
    s = Stack()
    balanced = True
    for i in string:
        if i == '(':
            s.push(i)
        elif i == ')':
            if s.is_empty():
                balanced = False
            else:
                s.pop()
    if s.is_empty() and balanced:
        return True
    else:
        return False
    
# Checking Matching Bracket
def is_balanced_deep(string):
    s = Stack()
    balanced = True
    for i in string:
        if i in '({[':
            s.push(i)
        elif i in ')}]':
            if s.is_empty():
                balance =  False
            else:
                temp = s.pop()
                if not is_matched(temp, i):
                    balanced = False
    
    if s.is_empty() and balanced:
        return True
    else:
        return False

def is_matched(open, close):
    opens = '({['
    closes = ')}]'
    return opens.index(open) == closes.index(close)
    