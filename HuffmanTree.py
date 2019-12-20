import heapq

class Node:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None
        self.parent = None
        self.code = None
    
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
    
    def getCode(self):
        return self.code
    
    def setCode(self, code):
        self.code = code
        
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
    
    def assignCodes(self, root):
        if root.getCode() is None:
            if root.getLeft() is not None:
                root.getLeft().setCode("0")
                self.assignCodes(root.getLeft())
            
            if root.getRight() is not None:
                root.getRight().setCode("1")
                self.assignCodes(root.getRight())
        
        else:
            if root.getLeft() is not None:
                root.getLeft().setCode(root.getCode() + "0")
                self.assignCodes(root.getLeft())
            
            if root.getRight() is not None:
                root.getRight().setCode(root.getCode() + "1")
                self.assignCodes(root.getRight())
    
    def printCodes(self, root):
        if root.getData() is None:
            self.printCodes(root.getLeft())
            self.printCodes(root.getRight())
        
        else:
            print("{} - {} - {}".format(root.getData(), bin(int.from_bytes(root.getData().encode(), 'big')), root.getCode()))
    
    def getNBits(self, root):
        if root.getData() is None:
            return (self.getNBits(root.getLeft()) + self.getNBits(root.getRight()))
        else:
            #print("{} {} {}".format(root.getData(), root.getFrequency(), len(str(root.getCode()))))
            return (int(root.getFrequency()) * len(str(root.getCode())))