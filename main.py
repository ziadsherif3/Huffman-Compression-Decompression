import HuffmanTree
import heapq

def compress():
    char_freq_map = {}
    #Reading file and getting frequency of each character
    fileName = input("Enter the Name of the file: ")
    
    try:
        with open(fileName) as f:
            while True:
                c = f.read(1)
                if not c:
                    break
                
                if c in char_freq_map:
                    char_freq_map[c] = char_freq_map[c] + 1
                    continue
            
                char_freq_map[c] = 1
    except:
        print("Error while opening file.")
        return
    
    # for k,v in char_freq_map.items():
    #     print("{} : {}".format(k, v))
    minHeap = []
    #Building minimum heap
    for k,v in char_freq_map.items():
        node = HuffmanTree.Node(k, v)
        minHeap.append(node)
    
    heapq.heapify(minHeap)
    # for node in minHeap:
    #     print("{} : {}".format(node.data, node.freq))
    tree = HuffmanTree.Tree()
    root = tree.buildHuffmanTree(minHeap)
    tree.assignCodes(root)
    tree.printCodes(root)

def decompress():
    pass

def main():
    while True:
        action = input("1)Compress\n2)Decompress\n3)exit\n")
        if action == "1":
            compress()
        elif action == "2":
            decompress()
        elif action == "3":
            break
        else:
            print("Error")

if __name__ == "__main__":
    main()
