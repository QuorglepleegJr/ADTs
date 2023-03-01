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
        
        self.__data[self.__tail+1] = item
        self.__tail += 1

    def enqueue(self, *items):
        
        for item in items:

            self.__enqueue_single(item)
    
    def dequeue(self):
        
        item = self.front()
        
        self.__data[self.__head] = None
        self.__head += 1

        return item

class ReuseableLinearQueue(LinearQueue):

    def __enqueue_single(self, item):

        try:

            super(ReuseableLinearQueue, self).__enqueue_single(item)
        
        except QueueError:

            if self.__head == 0:

                raise QueueError("Queue has reached capacity")
            
            offset = 0
            index = 1

            while self.__data[index] is None:

                offset += 1
                index += 1
            
            for i in range(index, len(self.__data)):

                self.__data[i-offset] = self.__data[i]
            
            for i in range(offset):

                self.__data[-i] = None

q = ReuseableLinearQueue()
q.enqueue("A", "S", "M")
print(q.dequeue())
q.enqueue("F")
print(q.front())
print(q.dequeue())
for x in range(2):
    q.dequeue()
print(q.is_empty())
#q.front()
#q.dequeue()
q.enqueue(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)