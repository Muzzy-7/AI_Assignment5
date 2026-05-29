from tree import build_tree, assign_tree, print_tree

def heuristic_eval(node):
    """A mock heuristic function for internal nodes cut off by depth limit."""
    return 0 # In a real game, this evaluates board position. Here we just return 0.

def heuristic_alpha_beta(node, current_depth, target_depth, if_max, alpha=float('-inf'), beta=float('inf')):
    # 1. If we reach a leaf node
    if not node.children:
        return node.data
    
    # 2. If we reach the depth cutoff, return the heuristic value
    if current_depth == target_depth:
        node.data = heuristic_eval(node)
        return node.data

    # Standard Alpha-Beta Logic
    if if_max:
        best = float('-inf')
        for child in node.children:
            val = heuristic_alpha_beta(child, current_depth + 1, target_depth, False, alpha, beta)
            if val is not None:
                best = max(best, val)
                alpha = max(alpha, best)
            if beta <= alpha:
                break
        node.data = best
        return best
    else:
        best = float('inf')
        for child in node.children:
            val = heuristic_alpha_beta(child, current_depth + 1, target_depth, True, alpha, beta)
            if val is not None:
                best = min(best, val)
                beta = min(beta, best)
            if beta <= alpha:
                break
        node.data = best
        return best

if __name__ == "__main__":
    depth = int(input("Enter the FULL depth of the tree: "))
    branching_factor = int(input("Enter the branching factor: "))
    target = int(input("Enter the Depth Limit for the Heuristic cutoff: "))

    root = build_tree(depth, branching_factor)
    assign_tree(root)

    print("\nTree before Heuristic Alpha-Beta:")
    print_tree(root)

    heuristic_alpha_beta(root, 0, target, True) 

    print(f"\nTree after Heuristic Alpha-Beta (Cutoff at depth {target}):")
    print_tree(root)