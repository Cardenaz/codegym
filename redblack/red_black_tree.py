from collections import deque
#deque supports adding and removing elements 


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


class RedBlackTree: 
    def __init__(self): 
        self.root_node = None 
        self.steps = []


    def __str__(self): 
        return 'Steps of path is {} and root is {}'.format(self.steps, self.root_node)
       

    def insert(self, data): 
        node = Node(data)
        
        if self.root_node is None: 
            self.root_node = node 
            self.root_node.color = BLACK
            return self.root_node
        
       
        current = self.root_node
        parent = None
        while current != None:
            parent = current
            
            #node.parent = current
            if node.data < parent.data: 
                
                current = current.left_child
            else: 
                current = current.right_child


        node.parent = parent
        
        if (node.data < node.parent.data): 
            node.parent.left_child = node 
        else:
            node.parent.right_child = node
        self.helper_method_insert(node)
            
    
    def find_node_by_key(self, key):
        '''Helper function for removing an item. Similar to the 
        search function'''
        current = self.root_node 
        node_not_found = True
        while node_not_found: 
            if current.data == key: 
                return current
            elif current.data > key: 
                current = current.left_child
            else:
                current = current.right_child
        return current 

    def remove(self, key):
        node = self.find_node_by_key(key)
       # print("The node to delete is: ", node)
       # print('parent is ', node.parent)
        if node.left_child is None and node.right_child is None:
            if node.parent: #if node has a parent, check which child is the node: 
                if node == node.parent.right_child: 
                    node.parent.right_child = None 
                    x = None 
                else: 
                    node.parent.left_child = None
                    x = None
            else: #if node has no parent - root gets deleted 
                self.root_node = None
                x = None
        elif node.left_child is None and node.right_child != None: 
            node = node.right_child
            x = node.right_child
            
        elif node.left_child != None and node.right_child is None: 
            node = node.left_child
            x = node.left_child
        else: 
            x = node.right_child
        
        if x!= None: 
            self.removeHelper(x)
        
    def jennyInsert(self, data): 
        node = Node(data)
        if self.root_node is None:
            node.color = BLACK
            self.root_node = node
            return 

        current_node = self.root_node
        while current_node != None:
            parent_node = current_node
            if node.data < parent_node.data:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        node.parent = parent_node
        if node.parent.data > node.data: 
            node.parent.left_child = node 
        else:
            node.parent.right_child = node
        self.helper_method_insert(node)
        

        # If parent of inserted node is black, then it's done. 

    def isRed(self, node): 
        if node.color == RED: 
            return True
        else: 
            return False

    def removeHelper(self, x): 
        #Case 0: node x is red

        while x != self.root_node: 

            if x.color == RED: 
                x.color == BLACK 
                break  
            # Case 1: Color of x is black and its sibling red

            elif x == x.parent.left_child and x.color == BLACK:
                #if right-sibling is red do following: 
                sibling = x.parent.right_child
                if sibling.color == RED: 
                    sibling.color = BLACK
                    x.parent.color = RED
                    #if x is the left child do left rotation
                    self.rotate(x.parent, LEFT_ROTATE)
                    # set sibling to right child of parent 
                    sibling = x.parent.right_node   
                elif sibling.color == BLACK:
                    # three cases 
                    if sibling.right_child.color == BLACK and sibling.left_child.color == BLACK:
                        sibling.color = RED
                        x = x.parent 
                        if x.color == RED: 
                            x.color = BLACK 
                    elif sibling.left_child.color == RED and sibling.right_child.color == BLACK:
                        sibling.left_child.color = BLACK
                        sibling.color = RED 
                        self.rotate(sibling, RIGHT_ROTATE)
                        sibling = x.parent.right_child
                    elif sibling.right_child.color == RED:
                        color_of_x_parent = x.parent.color 
                        sibling.color = color_of_x_parent
                        x.parent.color = BLACK
                        sibling.right_child.color = BLACK 
                        self.rotate(x.parent, LEFT_ROTATE)
            elif x == x.parent.right_child and x.color == BLACK:
                #if left-sibling is red do following:
                sibling = x.parent.left_child
                if sibling.color == RED: 
                    sibling.color = BLACK
                    x.parent.color = RED 
                    #if x is the right child do right rotation
                    self.rotate(x.parent, RIGHT_ROTATE) 
                    # set sibling to the left child of parent 
                    sibling = x.parent.left_node 
            # With updated x and sibling we now proceed forward:
                elif sibling.color == BLACK:
                    if sibling.right_child.color == BLACK and sibling.left_child.color == BLACK:
                        sibling.color = RED
                        x = x.parent 
                        if x.color == RED: 
                            x.color = BLACK 
                    elif sibling.right_child.color == RED and sibling.left_child.color == BLACK:
                        sibling.right_child.color = BLACK
                        sibling.color = RED
                        self.rotate(sibling, LEFT_ROTATE)
                        sibling = x.parent.left_child
                    elif sibling.left_child.color == RED:
                        color_of_x_parent = x.parent.color
                        x.parent.color = BLACK 
                        sibling.left_child.color = BLACK 
                        self.rotate(x.parent, RIGHT_ROTATE)
        self.root_node.color = BLACK        
           
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
            
            offspring.right_child = node #Set the right child to previous grandparent
            node.parent = offspring #Update parent of grandparent to the root-node

    def helper_method_insert(self, node): 
        ''' Is invoked when inserting a new node. It checks the parent and 
        grandparents of the inserted node. The current_node variable helps us track 
        when the root of the tree is reached. 
        '''
        current_node = node
        while node.parent.color == RED:
            #check if the parent of the node is the right child of the grandparent. 
            if node.parent == node.parent.parent.right_child:
                uncle = node.parent.parent.left_child
                # if the color of uncle is red then only do recoloring, 
                # if the color of uncle is black, rotate. 
                
                if uncle != None and uncle.color == RED:
                    uncle.color = BLACK
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    current_node = node.parent.parent
                else:
                
                    if(node == node.parent.left_child):
                        current_node = node.parent
                        node = node.parent
                        self.rotate(node, RIGHT_ROTATE)   
                    node.parent.color = BLACK 
                    node.parent.parent.color = RED 
                    self.rotate(node.parent.parent, LEFT_ROTATE)             
            else:
                uncle = node.parent.parent.right_child
                
                if uncle != None and uncle.color == BLACK: 
                    uncle.color = 0
                    node.parent.color = BLACK 
                    node.parent.parent.color = RED 
                    current_node = node.parent.parent
                else: # Uncle is None, rotate left and then rotate right: 
                    if(node == node.parent.right_child):
                        node = node.parent #must update the object's value otherwise it will rotate higher up in the tree. 
                        self.rotate(node, LEFT_ROTATE)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                   
                    self.rotate(node.parent.parent, RIGHT_ROTATE)
            if current_node == self.root_node: 
                break 
        self.root_node.color = BLACK 
           
    def min(self): 
        current = self.root_node 
        while current.left_child: 
            current = current.left_child 
       
        return current 

    def max(self): 
        current = self.root_node
        while current.right_child: 
            current = current.right_child
       
       
        return current 

    def search(self, value):


        '''Searches for a value and returns True if it exists in 
        the Red Black Tree.'''
        assert value != None 
        candidate = self.root_node
        item_found = False
        node_not_found = True 
        try:
            while node_not_found:
                if candidate == None: 
                    return item_found 
                elif candidate.data == value:
                    item_found = True
                    return item_found
                elif candidate.data > value: 
                    #if value is smaller it should visit to the left. 
                    candidate = candidate.left_child
                elif candidate.data < value:
                    #if value is greater it should visit to the right.
                    candidate = candidate.right_child  
        except Exception:
            print('Value does not exist')
            
    def path(self, value): 
        start = self.root_node
        self.steps.append(start)
        while start.data != value: 
            if value > start.data:
                start = start.right_child
                self.steps.append(start)
            elif value < start.data: 
                start = start.left_child
                self.steps.append(start)
        return self.steps
            
    def bfs(self):
        ''' Returns an array of visited nodes'''
        array= []
        queue_nodes = deque([self.root_node])
        while len(queue_nodes) > 0:
            node = queue_nodes.popleft() # popleft() takes O(1) which is faster than pop(0) which takes O(n)
            array.append(node)
            #needs to visit both sides of the root node
            #if child exists,then add it to the queue
            if node.left_child is not None: 
                queue_nodes.append(node.left_child)
            if node.right_child is not None: 
                queue_nodes.append(node.right_child)
        return array



tree = RedBlackTree() 
tree.insert(10)
tree.insert(18)
tree.insert(7)
tree.insert(15)
tree.insert(16)
tree.insert(30)
tree.insert(25)
tree.insert(40)
tree.insert(60)
tree.insert(2)
tree.insert(1)
tree.insert(70)




    


        

