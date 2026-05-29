from tree import build_tree, assign_tree, print_tree

def min_max(node, if_max):
    if not node.children:
        return node.data

    values = []
    for child in node.children:
        values.append(min_max(child, not if_max))
    
    if if_max:
        node.data = max(values)
    else:
        node.data = min(values)
    
    return node.data

if __name__ == "__main__":
    depth = int(input("Enter the depth (root = depth 0) for your Minimax tree: "))
    branching_factor = int(input("Enter the branching factor: "))

    root = build_tree(depth, branching_factor)
    assign_tree(root)

    print("\nTree before Minimax:")
    print_tree(root)

    result = min_max(root, True) 

    print("\nTree after Minimax (Optimal value at root):")
    print_tree(root)