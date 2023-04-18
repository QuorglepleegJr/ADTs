class TreeError(Exception):

    pass

class Node():

    def __init__(self, value, children=None, parent=None):

        self._value = value

        if children is None:
            children = []
        
        self._children = children
        self._parent = parent

class BinaryNode(Node):

    def __init__(self, value, children=None):

        super().__init__(value, children)

        if len(self._children) > 2:

            raise TreeError("Cannot create binary node with >2 children")

        while len(self._children) < 2:

            self._children.append(None)
        
    def set_left_child(self, child):

        self._children[0] = child
        if self._children[0] is None: return
        self._children[0]._parent = self
    
    def set_right_child(self, child):

        self._children[1] = child
        if self._children[1] is None: return
        self._children[1]._parent = self

    def set_value(self, value):

        self._value = value        
    
    def get_left_child(self):

        return self._children[0]
    
    def get_right_child(self):

        return self._children[1]

    def get_value(self):

        return self._value


class BinaryTree():

    def __init__(self, initial_state=None):

        if initial_state is None:

            return
        
        rows = 0

        while 2**rows - 1 < len(initial_state):

            rows += 1
        
        while len(initial_state) < 2**rows - 1:

            initial_state.append(None)
        
        nodes = [None]

        for datum in initial_state:

            nodes.append(BinaryNode(datum))
        
        
        for row_index in range(rows-1):

            for value in range(2**row_index):

                left = nodes[(2**row_index + value)*2]
                right = nodes[(2**row_index + value)*2 + 1]

                if left.get_value() is None: left = None
                if right.get_value() is None: right = None

                nodes[2**row_index + value].set_left_child(left)
                nodes[2**row_index + value].set_right_child(right)
        
        self.root = nodes[1]
    
    def traverse(root, mode=0):

        if root is None: return

        if mode == 0: BinaryTree.__pre_traverse(root)
        if mode == 1: BinaryTree.__in_traverse(root)
        if mode == 2: BinaryTree.__post_traverse(root)
    
    def __pre_traverse(root):

        if root is None: return

        print(root.get_value())
        BinaryTree.__pre_traverse(root.get_left_child())
        BinaryTree.__pre_traverse(root.get_right_child())

    
    def __in_traverse(root):

        
        if root is None: return

        BinaryTree.__in_traverse(root.get_left_child())
        print(root.get_value())
        BinaryTree.__in_traverse(root.get_right_child())

    def __post_traverse(root):

        if root is None: return

        BinaryTree.__post_traverse(root.get_left_child())
        BinaryTree.__post_traverse(root.get_right_child())
        print(root.get_value())


if __name__ == "__main__":

    with open("BinaryTreeTests.txt", "r") as tests:

        for test in tests.readlines():

            b = BinaryTree(eval(test))

            print(f"\nTest: {test}\n")

            for i in range(3):

                BinaryTree.traverse(b.root, mode=i)
                print()
