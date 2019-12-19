class Node:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
    def __lt__(self, other):
        return self.freq < other.freq