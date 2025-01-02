class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_paths(root):
    if root:
        print('Root Data = ', root.data)
        find_paths(root.left)     # recur on left node
        find_paths(root.right)    # recur on right node

# driver code
if __name__ == '__main__':

    root       = TreeNode(12)
    root.left  = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left   = TreeNode(4)
    root.right.left  = TreeNode(10)
    root.right.right = TreeNode(5)
    find_paths(root)