from math import inf

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

    def __enqueue_single(self, item):
        pass

    def enqueue(self, *items):
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
    
    def __shuffle_to_front(self):

        if self.__head == 0:

                raise QueueError("Cannot enqueue to queue beyond capacity")
            
        offset = self.__head
        index = self.__head
        
        for i in range(index, len(self.__data)):

            self.__data[i-offset] = self.__data[i]
        
        self.__head -= offset
        self.__tail -= offset

    def __enqueue_single(self, item):

        if self.__tail == len(self.__data)-1:

            self.__shuffle_to_front()
        
        self.__tail += 1
        self.__data[self.__tail] = item
    
    def enqueue(self, *items):

        for item in items:

            self.__enqueue_single(item)
    
    def dequeue(self):
        
        item = self.front()

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

class PriorityQueue():

    # Constructor

    def __init__(self, capacity):
        pass

    # Methods

    def is_empty(self):
        pass

    def top(self):
        pass

    def __enqueue_single(self, item, priority):
        pass

    def enqueue(self, *items):
        pass

    def dequeue(self):
        pass

class NaivePriorityQueue(PriorityQueue):

    # Constructor

    def __init__(self, capacity):

        self.__data = [(None, -inf)] * capacity
    
    # Methods

    def is_empty(self):

        return self.__data[0][1] == -inf
    
    def top(self):

        if self.is_empty():

            raise QueueError("Cannot access top of empty priority queue")

        return self.__data[0][0]

    def __enqueue_single(self, item, priority):

        if self.__data[len(self.__data)-1][1] != -inf:

            raise QueueError("Cannot enqueue to queue beyond capacity")

        index = 0

        while self.__data[index][1] >= priority:

            index += 1
        
        self.__data = self.__data[:index] + \
            [(item, priority)] + self.__data[index:-1]
    
    def enqueue(self, *items):

        for item in items:

            self.__enqueue_single(item[0], item[1])
    
    def dequeue(self):

        item = self.top()

        self.__data = self.__data[1:] + [(None, -inf)]

        return item
    
class HeapPriorityQueue(PriorityQueue):

    # Constructor

    def __init__(self, capacity):

        self.__data = [(None, inf)] + [(None, -inf)] * capacity
        self.__end_index = 0
    
    # Methods

    def is_empty(self):

        return self.__end_index == 0
    
    def top(self):

        if self.is_empty():

            raise QueueError("Cannot access top of empty priority queue")
        
        return self.__data[1][0]

    def __enqueue_single(self, item, priority):

        self.__end_index += 1

        if self.__end_index == len(self.__data):

            raise QueueError("Cannot enqueue to queue beyond capacity")

        self.__data[self.__end_index] = (item, priority)

        problem_index = self.__end_index

        while self.__data[problem_index][1] > self.__data[problem_index//2][1]:

            temp = self.__data[problem_index]

            self.__data[problem_index] = self.__data[problem_index//2]

            self.__data[problem_index//2] = temp

            problem_index //= 2
    
    def enqueue(self, *items):

        for item in items:

            self.__enqueue_single(item[0], item[1])

    def dequeue(self):

        item = self.top()

        self.__data[1] = self.__data[self.__end_index]
        self.__data[self.__end_index] = (None, -inf)

        problem_index = 1

        max_priority = -inf

        max_index = 1
        
        for index in [problem_index, problem_index * 2, problem_index * 2 + 1]:

            if index < len(self.__data):

                if self.__data[index][1] > max_priority:

                    max_priority = self.__data[index][1]
                    max_index = index

        while max_index != problem_index:

            temp = self.__data[max_index]
            self.__data[max_index] = self.__data[problem_index]
            self.__data[problem_index] = temp

            problem_index = max_index

            max_priority = -inf

            max_index = 1
            
            for index in [problem_index, problem_index * 2, problem_index * 2 + 1]:

                if index < len(self.__data):

                    if self.__data[index][1] > max_priority:

                        max_priority = self.__data[index][1]
                        max_index = index
        
        self.__end_index -= 1
        
        return item

q = HeapPriorityQueue(8)
q.enqueue((5,5),(3,3),(2,2),(8,8))
print(q.dequeue())