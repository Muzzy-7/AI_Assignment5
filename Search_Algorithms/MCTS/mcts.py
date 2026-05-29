import math
import random
from tree import build_tree, assign_tree, print_tree

def select_promising_node(node):
    """Uses UCB1 to select the best child node."""
    best_value = float('-inf')
    best_node = None
    
    for child in node.children:
        if child.visits == 0:
            return child
            
        exploitation = child.score / child.visits
        exploration = math.sqrt(2 * math.log(node.visits) / child.visits)
        ucb_value = exploitation + exploration
        
        if ucb_value > best_value:
            best_value = ucb_value
            best_node = child
            
    return best_node

def simulate_random_playout(node):
    """Walks randomly down the tree until it hits a leaf node."""
    current = node
    while current.children:
        current = random.choice(current.children)
    return current.data 

def backpropagate(path, result):
    """Updates visits and scores for all nodes in the path."""
    for node in path:
        node.visits += 1
        node.score += result

def mcts(root, iterations):
    for _ in range(iterations):
        # 1. Selection
        current = root
        path = [current]
        
        while current.children and all(c.visits > 0 for c in current.children):
            current = select_promising_node(current)
            path.append(current)
            
        # 2. Expansion
        if current.children:
            unvisited = [c for c in current.children if c.visits == 0]
            current = random.choice(unvisited)
            path.append(current)
            
        # 3. Simulation
        leaf_value = simulate_random_playout(current)
        
        # 4. Backpropagation
        backpropagate(path, leaf_value)
        
    def assign_mcts_values(node):
        if node.children:
            node.data = round(node.score / node.visits, 2) if node.visits > 0 else None
            for child in node.children:
                assign_mcts_values(child)
                
    assign_mcts_values(root)
    return max(root.children, key=lambda c: c.visits).data if root.children else root.data

if __name__ == "__main__":
    depth = int(input("Enter the depth for your MCTS tree: "))
    branching_factor = int(input("Enter the branching factor: "))
    iterations = int(input("Enter number of MCTS iterations (e.g., 100): "))

    root = build_tree(depth, branching_factor)
    assign_tree(root)

    print("\nTree before MCTS:")
    print_tree(root)

    mcts(root, iterations) 

    print("\nTree after MCTS (Internal nodes = average values):")
    print_tree(root)