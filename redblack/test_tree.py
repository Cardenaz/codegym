#Binary search tree 
import random as random


RED = 'RED'
BLACK = 'BLACK'
LEFT_ROTATE = 'LEFT_ROTATE'
RIGHT_ROTATE = 'RIGHT_ROTATE'

class Node: 
    def __init__(self, data): 
        self.data = data
        self.right_child = None 
        self.left_child = None 
        self.parent = None
        self.color = RED

    def __str__(self): 
        return 'Node of {} color is {})'.format(self.data, self.color)


class Tree: 
    def __init__(self): 
        self.root_node = None 

    def insertdos(self, data): 
        node = Node(data)
        if self.root_node is None: 
            self.root_node = node 
            self.root_node.color = 'BLACK'
            return 
        else: 
            current = self.root_node
            parent = None 
            while True: 
                parent = current 
                if node.data < parent.data: 
                    current = current.left_child
                    if current is None: 
                        parent.left_child=node
                       #return
                else: 
                    current = parent.right_child
                    if current is None: 
                        parent.right_child = node   
                       # return 
                try:
                    self.helper_method_insert(node)
                except AttributeError: 
                    pass 
                

    def insert(self, data): 
        node = Node(data)
        print(node.data)
        if self.root_node is None: 
            self.root_node = node 
            self.root_node.color = BLACK
            return self.root_node
        
       
        current = self.root_node
        parent = None
        while current != None:
            parent = current
            print('parent: ', parent)
            #node.parent = current
            if node.data < parent.data: 
                print(current.left_child)
                current = current.left_child
            else: 
                current = current.right_child


        node.parent = parent
        
        if (node.data < node.parent.data): 
            node.parent.left_child = node 
        else:
            node.parent.right_child = node
        self.helper_method_insert(node)
            
                 

        


            

               
           
    def rotate(self, node, mode):
        ''' Rotates according to the mode. Switches subtrees to maintain 
        the red-black-tree properties. '''
        if mode == 'LEFT_ROTATE': 
            offspring = node.right_child
          #  node_right_child = offspring.left_child
            if offspring.left_child is not None: 
                offspring.left_child.parent = node 
            offspring.parent = node.parent
            #Check if not root. 
            if offspring.parent is None:
                self.root_node = offspring
            elif node == node.parent.left_child: 
                node.parent.left_child = offspring
            else:
                node.parent.right_child = offspring
            offspring.left_child = node 
            node.parent = offspring
        elif mode == 'RIGHT_ROTATE':
            offspring = node.left_child
          #  node.left_child = offspring.right_child 
            if offspring.right_child is not None: 
                offspring.left_child.parent = node 
            offspring.parent = node.parent 

            if offspring.parent is None:
                self.root_node = offspring
            elif node == node.parent.right_child: 
                node.parent.right_child = offspring
            else:
                node.parent.left_child = offspring
            offspring.right_child = node 
            node.parent = offspring

    def helper_method_insert(self, node): 
        ''' Is invoked when inserting a new node. It checks the parent and 
        grandparents of the inserted node. The current_node variable helps us track 
        when the root of the tree is reached. 
        '''
        current_node = node
       # parent_color = node.parent.color
        #current_node != self.root_node: 
        while node.parent.color == RED:
            
            if node.parent.parent is not None: 

                #check if the parent of the node is the right child of the grandparent. 
                if node.parent == node.parent.parent.right_child:
                    uncle = node.parent.parent.left_child
                    # if the color of uncle is red then only do recoloring, 
                    # if the color of uncle is black, rotate. 
                    if uncle.color == RED:
                        uncle.color = BLACK
                        node.parent.color = BLACK
                        node.parent.parent.color = RED
                        current_node = node.parent.parent
                    else:
                    
                        if(node == node.parent.left_child):
                            #node = node.parent 
                            self.rotate(node.parent, LEFT_ROTATE)   
                        node.parent.color = BLACK 
                        node.parent.parent.color = RED 
                        self.rotate(node.parent.parent, RIGHT_ROTATE)             
                else:
                    uncle = node.parent.parent.right_child
                    if uncle.color == BLACK: 
                        uncle.color = 0
                        node.parent.color = BLACK 
                        node.parent.parent = RED 
                        current_node = node.parent.parent
                    else:
                        if(node == node.parent.right_child):
                            self.rotate(node.parent, RIGHT_ROTATE)
                        node.parent.color = BLACK
                        node.parent.parent.color = RED
                        self.rotate(node.parent.parent, RIGHT_ROTATE)
            if node == self.root_node: 
                break 
        self.root_node.color = BLACK 
        

        
        


            

    def find_min(self): 
        current = self.root_node 
        while current.left_child: 
            current = current.left_child 
        print(current.data)
        return current 

    def find_max(self): 
        current = self.root_node
        while current.right_child: 
            current = current.right_child
        print(current.data)
        testnode = current.parent
        print(testnode)
        print(testnode.parent)
        return current 

tree = Tree() 
tree.insert(5)
#print(tree.root_node.color)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(11)
tree.find_max()



    
   

    


        

