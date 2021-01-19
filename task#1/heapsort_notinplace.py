class Heap: 

    def __init__(self): 
        self.heap = [0]
        self.length = 0 
    def __repr__(self): 
        return str(self.heap)
    def add(self, value):
        #1. add 
        #2. increase length of list
        #3. make sure tree is balanced
        self.heap.append(value)
        self.length += 1 
        self.balanceTree(self.length)  
    def pop(self): 
        minimum_value = self.heap[1]
        self.heap[1] = self.heap[self.length]
        self.length = self.length -1 
        self.heap.pop()
        self.bubble(1)
        return minimum_value
    def index(self, value):
        if value * 2 + 1 > self.length: 
            value = value * 2 
        elif self.heap[value*2] < self.heap[value*2+1]:
            value  = value * 2
        else: 
            value = value * 2 +1 
        return value
    def bubble(self, value):
        while value*2 <= self.length:
            comparison = self.index(value)
            if self.heap[value] > self.heap[comparison]: 
                self.heap[value], self.heap[comparison] = self.heap[comparison], self.heap[value],
            
            value = comparison
    def balanceTree(self, value): 
        #balance while reaching the root node 
        while (value//2) > 0: 
            if self.heap[value] < self.heap[value//2]:
                #swap values between child and parent
                self.heap[value], self.heap[value//2] = self.heap[value//2], self.heap[value]
            #half of value 
            value = value//2 
   
def heapsort_notinplace(array): 
    heap = Heap()
    sorted_list = []
    for item in array: 
        heap.add(item)
    for i in range(heap.length): 
        minimum_value = heap.pop()
        sorted_list.append(minimum_value)
    return sorted_list










      
