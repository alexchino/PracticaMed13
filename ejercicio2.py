#Diseña un programa en Python que simule la atención de clientes en un banco. La atención
#debe seguir el principio "primero en llegar, primero en ser atendido" (FIFO - First In, First
#Out) utilizando una estructura de cola.?

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Error: La cola está vacía"
        return self.queue.popleft()

    def get_size(self):
        return len(self.queue)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue()) # Output: 1