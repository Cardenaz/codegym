from enum import Enum 

class Color(Enum): 
    '''represents the color of a Node object'''
    BLACK = "BLACK"
    RED = "RED"
    

class Node(object): 
    def __init__(self, key):
        self.key = key 
        self.parent = None 
        self.left_child = None
        self.right_child = None 
        self.color = Color.RED 

    def __str__(self): 
        return 'Node of {} with color: {})'.format(self.key, self.color.value)



class RedBlackTree(object): 
    def __init__(self) :
        self.root = None 
        self.nodes = []
      


    def insert(self, key):
        new_node = Node(key)
        if self.root == None: 
            self.root = new_node
            self.root.color = Color.BLACK
            self.nodes.append(self.root)
            return
        else:
            pass
            

           
            





        




        












    



