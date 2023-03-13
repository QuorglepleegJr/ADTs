class Stack():

    def __init__(self, *data):

        self.__data = [val for val in data]
    
    def pop(self):

        return self.__data.pop()

    def push(self, item):

        self.__data.append(item)
    
    def is_empty(self):

        return len(self.__data) == 0