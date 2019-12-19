import heapq

class Node:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None
        self.parent = None
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def getLeft(self):
        return self.left
    
    def setLeft(self, n):
        self.left = n
    
    def getRight(self):
        return self.right
    
    def setRight(self, n):
        self.right = n
    
    def getParent(self):
        return self.parent
    
    def setParent(self, n):
        self.parent = n
    
    def getData(self):
        return self.data
    
    def getFrequency(self):
        return self.freq
        
class Tree:
    def buildHuffmanTree(self, minHeap):
        while(len(minHeap) > 1):
            left = heapq.heappop(minHeap)
            right = heapq.heappop(minHeap)
            
            top = Node(None, left.getFrequency() + right.getFrequency())
            top.setLeft(left)
            top.setRight(right)
            left.setParent(top)
            right.setParent(top)
            heapq.heappush(minHeap, top)
        return heapq.heappop(minHeap)
    
    def printTree(self, root):
        if root.getData() is not None:
            print("{} : ".format(root.getData()), end = '')
        
        print(root.getFrequency())
        
        if root.getLeft() is not None:
            self.printTree(root.getLeft())
        
        if root.getRight() is not None:
            self.printTree(root.getRight())
        