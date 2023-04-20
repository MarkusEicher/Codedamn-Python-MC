from queue import Queue
from queue import PriorityQueue

q = Queue() # FIFO First In First Out

q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
# print(q.get_nowait())

q2 = PriorityQueue() # FIFO First In First Out with priorities

q2.put((2, "a"))
q2.put((1, "b"))
q2.put((3, "c"))
q2.put((4, "d"))
q2.put((5, "e"))

print(q2.get())
print(q2.get())

