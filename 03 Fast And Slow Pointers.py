# Detect if there is a loop in the linked list
# using slow and fast pointer technique

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(data):
    if not data:
        print('Linked List is empty. No cycle')
        return False

    slow = data
    fast = data.next

    while slow and fast.next:
        if slow == fast:
            print('Cycle is found')
            print('cycle length =', calculate_cycle_length(slow))
            return True
        slow = slow.next
        fast = fast.next.next

    return False

def calculate_cycle_length(slow):
    current      = slow
    cycle_length = 0
    while (True):
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length

# Driver Code
if __name__ == '__main__':
    # Creating Brute force linked list with a cycle
    head = Node(3)
    head.next = Node(2)
    head.next.next = Node(0)
    head.next.next.next = Node(-4)
    head.next.next.next.next = Node(6)
    head.next.next.next.next.next = Node(5)
    head.next.next.next.next.next.next = head.next

    isCycle = has_cycle(head)
    print('Output of the cycle test :', isCycle)