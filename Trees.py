from operator import *

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

    def __init__(self, value=None):

        super().__init__(value)

        self._children = [None,None]
        
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

    def __init__(self):

        self.root = None
    
    def from_array(array):

        if array is None:

            return
        
        rows = 0

        while 2**rows - 1 < len(array):

            rows += 1
        
        while len(array) < 2**rows - 1:

            array.append(None)
        
        nodes = [None]

        for datum in array:

            nodes.append(BinaryNode(datum))
        
        
        for row_index in range(rows-1):

            for value in range(2**row_index):

                left = nodes[(2**row_index + value)*2]
                right = nodes[(2**row_index + value)*2 + 1]

                if left.get_value() is None: left = None
                if right.get_value() is None: right = None

                nodes[2**row_index + value].set_left_child(left)
                nodes[2**row_index + value].set_right_child(right)
        
        tree = BinaryTree()
        tree.root = nodes[1]
        
        return tree
    
    def traverse(root, mode=0):

        if root is None: return

        if mode == 0: BinaryTree._pre_traverse(root)
        if mode == 1: BinaryTree._in_traverse(root)
        if mode == 2: BinaryTree._post_traverse(root)
    
    def _pre_traverse(root):

        if root is None: return

        print(root.get_value())
        BinaryTree._pre_traverse(root.get_left_child())
        BinaryTree._pre_traverse(root.get_right_child())

    
    def _in_traverse(root):

        
        if root is None: return

        BinaryTree._in_traverse(root.get_left_child())
        print(root.get_value())
        BinaryTree._in_traverse(root.get_right_child())

    def _post_traverse(root):

        if root is None: return

        BinaryTree._post_traverse(root.get_left_child())
        BinaryTree._post_traverse(root.get_right_child())
        print(root.get_value())

class BinarySearchTree(BinaryTree):

    def from_array(array):

        nodes = []

        for index in range(len(array)):

            nodes.append(BinaryNode(array[index]))

            if index > 0:

                BinarySearchTree.add_new_child(nodes[0], nodes[index])
        
        tree = BinarySearchTree()
        tree.root = nodes[0]

        return tree

    def add_new_child(origin, child):

        if child.get_value() > origin.get_value():

            if origin.get_right_child() is None:

                origin.set_right_child(child)
                return
            
            BinarySearchTree.add_new_child(origin.get_right_child(), child)
        
        else:

            if origin.get_left_child() is None:

                origin.set_left_child(child)
                return
            
            BinarySearchTree.add_new_child(origin.get_left_child(), child)

class BinaryExpressionTree(BinaryTree):

    operators = {
        "+":add,
        "-":sub,
        "*":mul,
        "/":truediv,
        "//":divmod
    }

    def from_string(string):

        return BinaryExpressionTree.from_array(
            BinaryExpressionTree._convert_rpn_string_to_array(string))
    
    def from_array(array):

        return BinaryExpressionTree._from_rpn_array(array)

    def _convert_rpn_string_to_array(string):

        array = []

        for element in string[1:-1].split(","):

            pass
    
    def _from_rpn_array(array):

        pass

    def evaluate(inp):

        if isinstance(inp, BinaryExpressionTree):

            pass
        
        return BinaryExpressionTree._evaluate_array(inp)

    def _evaluate_array(array):

            stack = []

            for element in array:

                if callable(element):

                    b = stack.pop()
                    a = stack.pop()

                    stack.append(element(a,b))
                
                else:

                    stack.append(element)
            
            return stack.pop()


if __name__ == "__main__":

    print(BinaryExpressionTree.evaluate([9,4,add,3,2,mul,add]))

    # with open("BinaryTreeTests.txt", "r") as tests:

    #     for test in tests.readlines():

    #         if test[0] == "b":
                
    #             b = BinarySearchTree.from_array(eval(test[1:]))

    #         else:

    #             b = BinaryTree.from_array(eval(test))

    #         print(f"\nTest: {test}\n")

    #         for i in range(3):

    #             BinaryTree.traverse(b.root, mode=i)
    #             print()
