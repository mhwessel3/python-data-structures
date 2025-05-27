class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"TreeNode({self.value})"


def sortedArrToBST(arr):
    if not arr:
        return None

    root_idx = len(arr) // 2 
    root = TreeNode(arr[root_idx])

    root.left = sortedArrToBST(arr[0 : root_idx])
    root.right = sortedArrToBST(arr[root_idx + 1:])

    return root

def printBST(root, indent=0):
    if root: 
        printBST(root.right, indent + 4)
        print(" " * indent + str(root.value))
        printBST(root.left, indent + 4)

# Construct Binary Search Tree from a SORTED array
arr = [1, 2, 3, 4, 5, 6, 6]

bst = sortedArrToBST(arr)
printBST(bst)
