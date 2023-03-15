from Stacks import Stack

class HashError(Exception):
    
    pass

class HashTable():

    def __init__(self, capacity, hash=None):

        pass

    def contains(self, item):

        pass

    def insert(self, item):

        pass

    def remove(self, item):

        pass

class CustomHashTable(HashTable):

    def __init__(self, capacity, hash=None):

        self.__data = [None] * capacity
        
        if hash is None:
            
            hash = lambda x: x%capacity

        self.__hash = hash
    
    def contains(self, item):

        return self.__data[self.__hash(item)] == item
    
    def insert(self, item):

        index = self.__hash(item)

        if self.__data[index] is not None and self.__data[index] != item:

            raise HashError("Collision detected")
        
        self.__data[index] = item
    
    def remove(self, item):

        index = self.__hash(item)

        if self.__data[index] is not None and self.__data[index] != item:

            raise HashError("Removal collision detected")

        self.__data[index] = None

class OpenCustomHashTable(HashTable):

    def __init__(self, capacity, hash=None):

        self.__data = [(None, None, None)] * capacity * 2
        self.__MAX = capacity
        
        if hash is None:
            
            hash = lambda x: x%capacity
        
        self.__hash = hash
        self.__spare_stack = Stack(capacity)

    def __get_index(self, item):

        index = self.__hash(item)

        val = self.__data[index]

        while val[0] is not None:

            print(val, item, index)

            if val[0] == item:

                return index
            
            elif val[1] is None:
                
                return -1
            
            index = val[1]
            val = self.__data[index]

    def contains(self, item):

        return self.__get_index(item) != -1
    
    def insert(self, *items):

        for item in items:

            self.__insert_single(item)

    def __insert_single(self, item):

        index = self.__hash(item)
        prev_index = None

        while self.__data[index][0] is not None:

            print(index, self.__data[index])
            print(self.__spare_stack._Stack__data)

            prev_index = index

            index = self.__data[index][1]

            if index is None:

                index = self.__spare_stack.pop()

                if self.__spare_stack.is_empty():

                    self.__spare_stack.push(index+1)
                
                break
        
        try:

            self.__data[index] = (item, None, prev_index)

            if prev_index is not None:

                self.__data[prev_index] = (self.__data[prev_index][0], \
                        index, self.__data[prev_index][2])
        
        except IndexError:

            raise HashError("Hash table has run out of additional memory")

    def remove(self, *items):

        for item in items:

            self.__remove_single(item)

    def __remove_single(self, item):

        index = self.__get_index(item)

        if index == -1:

            raise HashError("Can't remove non-present value from hash table")

        if index >= self.__MAX:

            new_next = self.__data[index][1]

            if new_next is not None:

                self.__data[new_next] = (self.__data[new_next][0], \
                    self.__data[new_next][1], self.__data[index][2])
            
            prev = self.__data[index][2]
            self.__data[prev] = (self.__data[prev][0], \
                new_next, self.__data[prev][2])
            
            self.__spare_stack.push(index)
        

        temp_data = [x for x in self.__data[index]]
        self.__data[index] = (self.__data[index][0], None, None)

        if index < self.__MAX:

            replacement_ind = temp_data[1]

            if replacement_ind is not None:

                self.__data[index] = (self.__data[replacement_ind][0], \
                    self.__data[replacement_ind][1], None)

                self.__spare_stack.push(replacement_ind)

class ClosedCustomHashTable(HashTable):

    def __init__(self, capacity, hash=None):

        self.__data = [None] * capacity
        
        if hash is None:

            hash = lambda x: x%capacity
        
        self.__hash = hash
    
    def contains(self, item):

        pass

    def insert(self, item):

        pass

    def remove(self, item):
        
        pass
    
h = OpenCustomHashTable(20)
print(h.contains(51))
print("INSERTION")
h.insert(37, 91, 22, 51, 82, 31)
print(h.contains(51))
print("REMOVAL")
h.remove(82, 91)
h.remove(51)
print(h.contains(51))
print(h.contains(31))
print("INSERTION")
h.insert(111, 131, 151)
print("TABLE")
d = h._OpenCustomHashTable__data
for i, x in enumerate(d):
    print(i, x)
print(h._OpenCustomHashTable__spare_stack._Stack__data)