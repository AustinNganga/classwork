class CircularQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * CircularQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front] # just like an array, position of an element in an array e.g. arr[1]

    def enqueue(self,element):
       if self._size == len(self._data):
           self.resize(2 * len(self._data)) #doubles the queue size if queue is full


       tail = (self._front + self._size) % len(self._data) # garbage collection
       self._data[tail] = element
       self._size = self._size + 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty for a dequeue operation")
        front = (self._front + 1) % len(self._data)
        dequeued_element = self._data[self._front]

        self._data[self._front] = None # garbage collection
        self._size -=1 #decrease array by 1


        return dequeued_element


    def resize(self, new_capacity):
        pass

class Empty(Exception):
    pass

if __name__ == "__main__":
    object_queue = CircularQueue()
    insert_elements = [11,22,33,44,55,66,77,88,99,100,111,222,333,444]

    for element in insert_elements:
        object_queue.enqueue(element)
        print(f"added element:{element}")
        print(f"the new size of the queue: {len(object_queue)}")

    print("\n current queue representation")




