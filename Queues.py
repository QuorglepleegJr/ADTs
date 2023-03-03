class QueueError(Exception):

    pass

class Queue():

    # Constructor

    def __init__(self, capacity):
        pass

    # Methods

    def is_empty(self):
        pass

    def front(self):
        pass

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass

class LinearQueue(Queue):

    # Constructor

    def __init__(self, capacity=16):

        self.__data = [None] * capacity
        self.__head = 0
        self.__tail = -1

    # Methods

    def is_empty(self):
        
        return self.__head > self.__tail

    def front(self):
        
        if self.is_empty(): 
            
            raise QueueError("Cannot access front of empty queue")
        
        return self.__data[self.__head]

    def __enqueue_single(self, item):

        if self.__tail == len(self.__data)-1:

            raise QueueError("Cannot enqueue to queue beyond capacity")
        
        self.__tail += 1
        self.__data[self.__tail] = item

    def enqueue(self, *items):
        
        for item in items:

            self.__enqueue_single(item)
    
    def dequeue(self):
        
        item = self.front()

        self.__head += 1

        return item

class ReuseableLinearQueue(Queue):

    # Constructor

    def __init__(self, capacity=16):

        self.__data = [None] * capacity
        self.__head = 0
        self.__tail = -1

    # Methods

    def is_empty(self):
        
        return self.__head > self.__tail

    def front(self):
        
        if self.is_empty(): 
            
            raise QueueError("Cannot access front of empty queue")

        return self.__data[self.__head]

    def __enqueue_single(self, item):

        if self.__tail == len(self.__data)-1:

            if self.__head == 0:

                raise QueueError("Cannot enqueue to queue beyond capacity")
            
            offset = 0
            index = 1

            while self.__data[index] is None:

                offset += 1
                index += 1
            
            for i in range(index, len(self.__data)):

                self.__data[i-offset] = self.__data[i]
            
            self.__head -= offset
            self.__tail -= offset
        
        self.__tail += 1
        self.__data[self.__tail] = item
    
    def enqueue(self, *items):

        for item in items:

            self.__enqueue_single(item)
    
    def dequeue(self):
        
        item = self.front()

        self.__data[self.__head] = None
        self.__head += 1

        return item


class CircularQueue(Queue):

    # Constructor

    def __init__(self, capacity):

        self.__data = [None] * capacity
        self.__head = 0
        self.__tail = -1
        self.__count = 0
        self.__MAX = capacity
    
    # Methods

    def is_empty(self):

        return self.__count == 0
    
    def front(self):

        if self.is_empty():

            raise QueueError("Cannot get front of empty queue")

        return self.__data[self.__head]

    def __enqueue_single(self, item):

        if self.__count == self.__MAX:

            raise QueueError("Cannot enqueue to queue beyond capacity")

        self.__count += 1

        self.__tail += 1
        self.__tail %= self.__MAX
        self.__data[self.__tail] = item
    
    def enqueue(self, *items):

        for item in items:
            
            self.__enqueue_single(item)

    def dequeue(self):

        item = self.front()

        self.__head += 1
        self.__head %= self.__MAX

        self.__count -= 1

        return item