from collections import deque
from queue import Queue

#deque
q=deque()

q.append('Hola')
q.append('Mundo')
q.rotate()
print(q)
print(q.popleft())

#Queue

s= Queue()

s.put('Hola')
s.put('Mundo')

print(s.get())