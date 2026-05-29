from tree import build_tree, assign_tree, print_tree

def alpha_beta(node, if_max, alpha=float('-inf'), beta=float('inf')):
    if not node.children:
        return node.data

    if if_max:
        best = float('-inf')
        for child in node.children:
            val = alpha_beta(child, False, alpha, beta)
            if val is not None:
                best = max(best, val)
                alpha = max(alpha, best)
            if beta <= alpha:
                break # Beta Cutoff (Pruning)
        node.data = best
        return best
    else:
        best = float('inf')
        for child in node.children:
            val = alpha_beta(child, True, alpha, beta)
            if val is not None:
                best = min(best, val)
                beta = min(beta, best)
            if beta <= alpha:
                break # Alpha Cutoff (Pruning)
        node.data = best
        return best

if __name__ == "__main__":
    depth = int(input("Enter the depth for your Alpha-Beta tree: "))
    branching_factor = int(input("Enter the branching factor: "))

    root = build_tree(depth, branching_factor)
    assign_tree(root)

    print("\nTree before Alpha-Beta:")
    print_tree(root)

    alpha_beta(root, True) 

    print("\nTree after Alpha-Beta (Notice 'None' values where branches were pruned):")
    print_tree(root)