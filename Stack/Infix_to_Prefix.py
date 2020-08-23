import Stack

def infix_to_prefix(string):
    
    precedence = {}
    precedence['*'] = 3
    precedence['/'] = 3
    precedence['+'] = 2
    precedence['-'] = 2
    precedence['('] = 1
    
    result = ''
    s = Stack()
    for i in string:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or i in '0123456789':
            result = result + i
        elif i =='(':
            s.push(i)
        elif i ==')':
            temp = s.pop()
            while not temp == '(':
                result = result + temp
                temp = s.pop()
        else:
            while (not s.is_empty()) and (precedence[s.peek()] > precedence[i]):
                result = result + s.pop()
            s.push(i)
            
            