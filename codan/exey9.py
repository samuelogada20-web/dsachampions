def is_valid_bst(root, minimum=float('-inf'), maximum=float('inf')):
    if root is None:
        return True

    if root.val <= minimum or root.val >= maximum:
        return False

    return (
        is_valid_bst(root.left, minimum, root.val) and
        is_valid_bst(root.right, root.val, maximum)
    )


# Create a node
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Test 1: Valid BST
root1 = Node(8)
root1.left = Node(3)
root1.right = Node(10)
root1.left.left = Node(1)
root1.left.right = Node(6)
root1.right.right = Node(14)

# Test 2: Invalid BST
root2 = Node(8)
root2.left = Node(3)
root2.right = Node(10)
root2.right.left = Node(4)

# Test 3: Empty tree
root3 = None

# Test 4: Single node
root4 = Node(5)

# Test 5: Duplicate value
root5 = Node(8)
root5.left = Node(8)

# Test 6: Another valid BST
root6 = Node(10)
root6.left = Node(5)
root6.right = Node(15)
root6.left.left = Node(2)
root6.left.right = Node(7)
root6.right.left = Node(12)
root6.right.right = Node(20)


# Run test cases
print("Test 1:", is_valid_bst(root1))
print("Test 2:", is_valid_bst(root2))
print("Test 3:", is_valid_bst(root3))
print("Test 4:", is_valid_bst(root4))
print("Test 5:", is_valid_bst(root5))
print("Test 6:", is_valid_bst(root6))