import sys
import queue

print("queue:")

q = queue.Queue()

for i in range(15):
    q.put(i)

while not q.empty():
    print(q.get())

print("stack:")

s = queue.LifoQueue()

for i in range(15):
    s.put(i)

while not s.empty():
    print(s.get())

print("named tuple: ", sys.getsizeof(e))
print("named tuple: ", sys.getsizeof(f))

print("tuple: ", sys.getsizeof(g))
print("integer: ", sys.getsizeof(g[0]))
print("integer: ", sys.getsizeof(3))
print("double", sys.getsizeof(3.2987230576028765092163598235908235986))
print("list:", sys.getsizeof([4, 12]))