from collections import deque
import random

class Treenode:
    def __init__(self, data=None):
        self.data = data
        self.children = []
        # Added for MCTS functionality
        self.visits = 0
        self.score = 0

def build_tree(depth, branching_factor):
    node = Treenode()
    if depth == 0:
        return node
    for _ in range(branching_factor):
        node.children.append(build_tree(depth - 1, branching_factor))
    return node 

def assign_tree(node):
    """Assigns user input to leaf nodes."""
    if not node.children:
        node.data = int(input("Enter value for leaf node: "))
        return
    for child in node.children:
        assign_tree(child)

def print_tree(node):
    """Prints the tree using BFS (Level Order Traversal)."""
    if not node:
        return
    
    queue = deque([node])
    while queue:
        l_size = len(queue)
        for _ in range(l_size):
            current = queue.popleft()
            # Print None if a node was pruned or untouched
            print(f"{current.data} ", end="")
            for child in current.children:
                queue.append(child)
        print()