

from BinaryTreeWeighted import BinaryTreeWeighted


BinaryTreeWeighted.strict_checking = True


def extract(h):
    if (h.is_empty()):
        raise ValueError("Cannot extract from empty tree.")
        
    root = h[0]
    if (root.parent is None):
        return root
    
    
def insert(h, value):
    if (h.is_empty()):  
        h.value = value
        return
    elif (h.left is None):
        h.add_left(BinaryTreeWeighted(value))
    elif (h.right is None):
        h.add_right(BinaryTreeWeighted(value))
    else:
        if (is_full_subtree(h.left) is not True):
            insert(h.left, value)
        elif(is_full_subtree(h.right) is not True):
            insert(h.right, value)
        else: insert(h.left, value)
        
    h.weight += 1

def is_full_subtree(h):
    if (h is None):
        return True
    if (h.left is None and h.right is None):
        return True
    elif (h.left is not None and h.right is not None):
        return h.left.weight == h.right.weight and is_full_subtree(h.left) and is_full_subtree(h.right) 
    
    return False

# geeksforgeeks.org/dsa/check-whether-binary-tree-full-binary-tree-not/ - found steps walking through checking if a subtree is full
        
    