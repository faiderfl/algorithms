from queue import LifoQueue
from collections import deque

#LifoQueue
s= LifoQueue()
s.put('Hola')
s.put('Mundo')

print(s.get())

#deque
q=deque()

q.append('Hola')
q.append('Mundo')

print(q.pop())


## Example: (({()}))

def validate_structure(code_structure):
    lq=LifoQueue()
    
    for s in code_structure:
        if isOpen(s):
            lq.put(s)
        else:
            if closes(lq.get(s), s)!= True:
                return False
    return lq.empty()


def isOpen(s):
    characters= ['{','(','{']
    if s in characters: return True
    else: return False

def closes(lq, s):
    pairs = {'(':')','[':']','{':'}' }
    if (pairs[lq]==s):
        return True
    else:
        return False

print(validate_structure('(['))