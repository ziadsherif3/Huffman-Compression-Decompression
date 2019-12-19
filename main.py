import HuffmanTreeNode
import heapq

def main():
    char_freq_map = {}
    #Reading file and getting frequency of each character
    with open("input.txt") as f:
        while True:
            c = f.read(1)
            if not c:
                break
            if c in char_freq_map:
                char_freq_map[c] = char_freq_map[c] + 1
                continue
            char_freq_map[c] = 1
    # for k,v in char_freq_map.items():
    #     print("{} : {}".format(k, v))
    minHeap = []
    #Building minimum heap
    for k,v in char_freq_map.items():
        node = HuffmanTreeNode.Node(k, v)
        minHeap.append(node)
    heapq.heapify(minHeap)
    # for node in minHeap:
    #     print("{} : {}".format(node.data, node.freq))

if __name__ == "__main__":
    main()
