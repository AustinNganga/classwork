

class Circulararrayqueue:
    """
    A QUEUE AS DISCUSSED IN THE FIFO PRINCIPLE, FIRST IN FIRST OUT.

    This is a CIRCULAR QUEUE - imagine the array as a circle where after the last position, we wrap back to the first
    position.This prevents us from having to shift all elements when we remove/dequeue items from the front

    """
    # we start by defining the maximum no of elements that our queue will hold
    DEFAULT_CAPACITY = 10
    def __init__(self):
        """
        we continue to create an empty queue by initializing 3 important things:
        i._data: which is basically a list filled with None values, the array...
        ii.size: how many actual elements are at a given timestamp, we will initialize it to zero.
        iii.front: the index or the position where the first element is located, we initialize to zero too

        """
        # create a list/out array, with DEFAULT_CAPACITY slots, all filled with None. You can think of this as creating
        # 10 empty parking spaces in a circular park
        self._data = [None]*Circulararrayqueue.DEFAULT_CAPACITY

        #here we keep track of how many elements that are actually in the list.For this case the number of cars that are
        #actually parked
        self._size = 0

        #and here we keep track of the first car we parked at the lot
        self._front = 0

    def __len__(self):
        """
        This is an inbuilt constructor method or rather a dunder method, just like __init__.It returns the size of an
        attribute created in the primary constructor. In this case, it's the elements currently in the queue. This is
        like counting the number of cars we have in a circular parking lot

        """
        return self._size
    def is_empty(self):
        """
        This method will return a boolean, denoted by the double equal sign operator, which is a comparison operator.
        Thus, it will return true if the array is empty, including when it's filled None and false if it has at least
        one element.
        """
        return self._size == 0

    def first(self):
        """
        This method is analogous to the PEEK() method in stacks, which will return the element at the front of the queue
        without removing it. In our example, it's like looking at the first car to be parked at the lot without making it
        leave. Or a bank teller checking the first person in a queue soa s to be expectant who they are serving first
        The method will raise an empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("queue is empty") # how this exception is raised is by calling the class Exception and passing
            # the exception type/message
        # the front element is at position self._front in our array
        return self._data[self._front]

    def dequeue(self):
        """
        this method will remove and return the first element of the queue, fulfilling our principle FIFO, which is first
        in first out.
        Hre we have another concept as in Circularly Linked List, which is instead of shifting all elements left which
        is slow, we just move our _front pointer to the next position and use  MODULO arithmetic to wrap around when we
        reach the end of the array
        Of course you start by checking if the queue is empty
        """
        if self.is_empty():
            raise Empty("queue is empty")
        # here we get the element at the front of the queue, and save it in an attribute
        item_to_dequeue = self._data[self._front]
        # then clear the old front position to help with garbage collection, python will clean up the memory better this
        #way
        #garbage collection is a technique/process/procedure manual or autonomous, that handles memory allocation and
        # deallocation ensuring efficient use of memory. It is done manually in C and C++.Read more about it here
        #https://www.geeksforgeeks.org/garbage-collection-python/
        self._data[self._front] = None
        # here's the magic
        #Move the pointer to the next position
        #The modulo(%) operator makes it "wrap around", if we are at the last position then add 1, which will go back to
        # position 0 like a circular parking lot
        self._front = (self._front+1) % len(self._data)
        # we now have one less element in the queue, so remember to decrease the queue size by one
        self._size-=1
        """
        of course the method should return the dequeued element
        """
        return item_to_dequeue
    

    def enqueue(self,element):
        """
        This is adding an element to the rear/back of our queue
        This is like a new person joining the queue, which will be at the back of the line.
        AGAIN, here's the magic : we calculate where the "back" of the queue is, using modulo arithmetic: (front+size)%
        capacity.This automatically wraps around the array when needed

        """
        # we will start with an IS_FULL check, and if True we increase the size of our queue
        if self._size == len(self._data):
            self._resize(2 * len(self._data)) # double the capacity
        # calculate where to put the new element(at the back of the queue)
        #let me illustrate
        #if front=3, which means the head is at 3, and size = 4, which is the DEFAULT_CAPACITY, then back position =
        #(3+4)% 10 = 7
        # if front=8, which means the head is at 8, and size = 4, which is the DEFAULT_CAPACITY, then back position=
        # (8+4)% 10 = 2(which wraps around the queue)
        back_of_the_queue = (self._front+self._size) % len(self._data)

        #Place the new element at the newly obtained back position of our queue, where enqueuing takes place
        self._data[back_of_the_queue] = element

        #we now have one more element in the queue, thus we increment the size
        self._size+=1

    #what if the queue is full, but we still need to enqueue
    def _resize(self,new_capacity):
        """
        This method will double the size of our queue, only when there are no empty slots.The current size of the queue
        is multiplied by a factor specified by the user, in this case new_capacity
        You need to note that when we resize, we need to "unwrap" the circular structure/array and create a new linear
        arrangement starting from index 0 so that we can double the capacity quite easily
        """
        #create a new bigger array
        old_data = self._data# hold the existing data in our queue in the old_data attribute
        self._data = [None]*new_capacity# resizing the new_capacity factor
        #then we copy all elements from the old array/queue to the new one, starting from the front and going in the
        # queue order
        current_index = self._front
        for item in range(self._size):
            # copy each element to the new array in order
            self._data[item] = old_data[current_index]
            #move to the next element, and of course remember to wrap around if necessary
            current_index = (current_index + 1)%len(old_data)

        #finally we reset the front to position 0 since we have reorganized everything
        self._front = 0
# this is the class we  spoke of earlier, with a custom exception message for an empty queue operation
class Empty(Exception):
    # exception will be raised when trying to access elements from an empty queue
    def __init__(self, message = "queue is empty"):
        self.message = message
        super().__init__(self.message)

#after preparing the ingredients and the recipe, lets now put it into use
if __name__ == '__main__':#as discussed, this check is mostly used to avoid running the contents of this block when
    # imported into another file
    # create a new queue
    queue = Circulararrayqueue()
    print("QUEUES USING CIRCULAR ARRAYS")
    print(f"the initial queue size is: {len(queue)}")
    print(f"Is queue empty?{queue.is_empty()}")
    #ENQUEUE OUR QUEUE
    print("\n Enqueuing our queue")
    elements_to_enqueue = ["Alice", "Bob", "William","Dorothy","Jessica"]
    for person in elements_to_enqueue:
        queue.enqueue(person)
        print(f"Added {person}. Queue size is now {len(queue)}")

    #show the front element without removing it
    print(f"\n Person at the front of the line: {queue.first()}")

    #remove some elements/dequeue operations, then return it
    print("\n Serving people from the front of the queue: ")
    for i in range(3):
        served_person = queue.dequeue()
        print(f"Served: {served_person}. Queue size is now: {len(queue)}")

    # to demo the circular nature, we can induce an overflow and see if it behaves correctly
    print("\n Adding more people to induce a wrap around in the array")
    more_people = ["Frank", "Linda", "Ford"]

    for person in more_people:
        queue.enqueue(person)
        print(f"Added {person}. Queue size is now {len(queue)}")


    #show what is left in the queue
    print(f"\n Person currently at the front: {queue.first()}")
    print(f"total people still at the queue: {len(queue)}")

    #demonstrate the wrap around by showing internal state
    print(f"Internal details")
    print(f"Front index: {queue._front}")
    print(f"array contents: {queue._data}")

# NB None values are empty slots in our circular array












