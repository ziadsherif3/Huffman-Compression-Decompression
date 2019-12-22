import HuffmanTree
import heapq
import time

def compress():
    char_freq_map = {}
    fileName = input("Enter the Name of the file: ")
    file = ""
    
    #Reading file and getting frequency of each character
    try:
        with open(fileName) as f:
            while True:
                c = f.read(1)
                if not c:
                    break
                
                file = file + c
                
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
    
    # oldNBits = 0
    
    # for k,v in char_freq_map.items():
    #     oldNBits = oldNBits + (v * (len(str(bin(int.from_bytes(k.encode(), 'big')))) - 1))
    
    # print("Compression ratio = {}%".format((tree.getNBits(root) / oldNBits) * 100))
    
    HuffmanTree.writeCompressedFile(root, file, fileName)

def decompress():
    pass

def main():
    while True:
        action = input("1)Compress\n2)Decompress\n3)exit\n")
        if action == "1":
            start = time.time()
            compress()
            end = time.time()
            print("Execution time: {} secs".format(end - start))
        elif action == "2":
            start = time.time()
            decompress()
            end = time.time()
            print("Execution time: {}secs".format(end - start))
        elif action == "3":
            break
        else:
            print("Error")

if __name__ == "__main__":
    main()
