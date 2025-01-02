class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# reverse the list and return the head of the revered list
def reverse_list(node):
    # initialize three pointers : curr, next and prev
    curr = node
    prev = None
    next = None

    # traverse all the nodes of the linked list
    while curr is not None:

        next = curr.next     # store the next

        curr.next = prev     # reverse the node's next pointer

        prev = curr          # move pointers one position ahead
        curr = next

    # return the head of reversed linked list
    return prev

def print_linked_list(node):
    while(node):
        print(node.data, end =" ")
        node = node.next
    print()

# driver code
if __name__ == '__main__':

    # Create brute force hard-coded linked list
    head = Node(4)
    head.next = Node(5)
    head.next.next = Node(1)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(7)
    head.next.next.next.next.next = Node(2)

    print_linked_list(head)

    reverse = reverse_list(head)

    print('reversed linked list:', end= " ")
    print_linked_list(reverse)
