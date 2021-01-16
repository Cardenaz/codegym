from enum import Enum 

class Color(Enum): 
    '''represents the color of a Node object'''
    BLACK = 0
    RED = 1 
    

class Node(object): 
    def __init__(self, key):
        self.key = key 
        self.parent = None 
        self.leftNode = None
        self.rightNode = None 
        self.color = Color.RED 

    def __str__(self): 
        return 'Node of {} with color: {})'.format(self.key, self.color.value)

class RedBlackTree(object): 
    def __init__(self) :
        self.root = None 

    def insert(self, key):
        new_node = Node(key)
        if self.root == None: 
            self.root = new_node
            return
        else: 
            pass 


tree = RedBlackTree()
print(tree.root)
tree.insert(23) 
print(tree.root)



        




        












    



