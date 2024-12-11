def print_tree(node, prefix="", is_left=True, first_is_root=True):
    """
    Recursively print a binary tree with improved formatting and visual representation.
    
    Args:
        node: The current node to print
        prefix: Current indentation prefix for hierarchical display
        is_left: Flag to indicate if the current node is a left child
        first_is_root: Flag to handle root node special formatting
    """
    # Early return for None or leaf nodes
    if node is None:
        return
    
    # Determine connector and printing logic
    try:
        # Check if node has children
        has_children = hasattr(node, 'left') and hasattr(node, 'right')
        
        # Determine connector
        if first_is_root:
            connector = '  '
        else:
            connector = "├─ " if is_left else "└─ "
        
        # Prepare node representation
        if has_children:
            # For nodes with complex structure
            if (isinstance(node.left, str) and isinstance(node.right, str)):
                # Special case for leaf-like nodes with string children
                node_repr = f'{node.left} {node.operator} {node.right}'
            else:
                # Default to operator representation
                node_repr = str(node.operator)
        else:
            # For simple nodes or leaf nodes
            node_repr = str(node)
        
        # Print current node
        print(prefix + connector + node_repr)
        
        # Recursive traversal
        if has_children:
            # Prepare new prefix for children
            new_prefix = prefix + ("│  " if is_left else "   ")
            
            # Recursively print left child
            if node.left is not None:
                print_tree(node.left, new_prefix, is_left=True, first_is_root=False)
            
            # Recursively print right child
            if node.right is not None:
                print_tree(node.right, new_prefix, is_left=False, first_is_root=False)
    
    except AttributeError:
        # Fallback for unexpected node structures
        print(prefix + connector + str(node))

