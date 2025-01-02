# Level Order Traversal using QUEUE

class TreeNode:
    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None


def print_level_order(root):

    # check if the root has data
    if root is None:
        print("Root is empty. Nothing to print")
        return

    # create an empty queue for level order traversal
    queue = []

#    print(root.data)
    # enqueue root and initialize height
    queue.append(root)

    while (len(queue) > 0):
        print('length of the queue =', len(queue))
        # print front of queue and remove it from queue
        print('Queue Data is =', queue[0].data, end="\n")
        node = queue.pop(0)

        # enqueue left child
        if node.left is not None:
            queue.append(node.left)
        # enqueue right child
        if node.right is not None:
            queue.append(node.right)

# driver code
if __name__ == '__main__':

    print('Traversing one root Tree')
    print('-------------------------------')
    one_node_root =  TreeNode(1);
    print_level_order(one_node_root);

    print('Traversing Multi root Tree')
    print('-------------------------------')
    root       = TreeNode(3)
    root.left  = TreeNode(9);
    root.right = TreeNode(20);
    root.right.left  = TreeNode(15);
    root.right.right = TreeNode(7);

    print_level_order(root)
