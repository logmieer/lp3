import heapq
from collections import Counter

# Node class to represent nodes in the Huffman tree


class Node:
    def __init__(self, left=None, right=None, value=None, frequency=None):
        self.left = left
        self.right = right
        self.value = value
        self.frequency = frequency

    def children(self):
        return (self.left, self.right)

# Huffman_Encoding class to perform Huffman encoding


class Huffman_Encoding:
    def __init__(self, string):
        self.q = []  # Priority queue to hold nodes
        self.string = string  # Input string to be encoded
        self.encoding = {}  # Dictionary to store Huffman codes

    # Calculate the frequency of each character in the input string
    def char_frequency(self):
        count = {}
        for char in self.string:
            if char not in count:
                count[char] = 0
            count[char] += 1

        # Create nodes for each character and its frequency, and add them to the priority queue
        for char, value in count.items():
            node = Node(value=char, frequency=value)
            self.q.append(node)

        # Sort the nodes in the priority queue based on their frequencies
        self.q.sort(key=lambda x: x.frequency)

    # Build the Huffman tree by merging nodes with the lowest frequencies
    def build_tree(self):
        while len(self.q) > 1:
            n1 = self.q.pop(0)
            n2 = self.q.pop(0)
            node = Node(left=n1, right=n2,
                        frequency=n1.frequency + n2.frequency)
            self.q.append(node)
            self.q.sort(key=lambda x: x.frequency)

    # Helper function to generate Huffman codes for each character in the tree
    def helper(self, node: Node, binary_str=""):
        if type(node.value) is str:
            self.encoding[node.value] = binary_str
            return
        l, r = node.children()
        self.helper(node.left, binary_str + "0")
        self.helper(node.right, binary_str + "1")

    # Perform Huffman encoding by generating Huffman codes
    def huffman_encoding(self):
        root = self.q[0]
        self.helper(root, "")

    # Print the character and its corresponding Huffman code
    def print_encoding(self):
        print(' Char | Huffman code ')
        for char, binary in self.encoding.items():
            print("%-4r |%12s" % (char, binary))

    # Main method to perform the entire encoding process
    def encode(self):
        self.char_frequency()  # Calculate character frequencies
        self.build_tree()  # Build the Huffman tree
        self.huffman_encoding()  # Generate Huffman codes
        self.print_encoding()  # Print the results


# Input from the user
string = input("Enter string to be encoded: ")
encode = Huffman_Encoding(string)
encode.encode()  # Perform the Huffman encoding
