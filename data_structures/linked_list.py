class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        """Create a user-friendly string representation of the linked list."""
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values) + " -> None"

    def __repr__(self):
        """Create an official string representation of the ListNode."""
        return f"{self.__class__.__name__}(val={self.val}, next={repr(self.next)})"

    def __iter__(self):
        """Allow the ListNode to be iterable."""
        current = self
        while current:
            yield current.val
            current = current.next

def create_list(values):
    """Create a linked list from a list of values and return the head of the list."""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def swap_pairs(head: ListNode | None) -> ListNode | None:
    """Swap adjacent nodes within a linked list and return the head of the list"""
    # Base case: if the list is empty or has only one node
    if not head or not head.next:
        return head

    # Nodes to be swapped
    first_node = head
    second_node = head.next

    # Swapping
    first_node.next = swap_pairs(second_node.next)
    second_node.next = first_node

    # Now the head is the second node
    return second_node



def reverse(head: ListNode | None) -> ListNode | None:
    """Reverse the nodes with a linked list and return the head of the list.
    
    Example
        Initial List: 1 -> 2 -> 3 -> None

        After reverse(3):
        3 -> None

        After reverse(2):
        3 -> 2 -> None
        (Disconnect 2 from 1)

        After reverse(1):
        3 -> 2 -> 1 -> None
        (Disconnect 1 from original list)

        Final List: 3 -> 2 -> 1 -> None
    """

    # Base case: if the list is empty or has only one node there is nothing to reverse
    if not head or not head.next:
        return head
    
    # Recursive Step: reverse the rest of the list
    new_head = reverse(head.next)
    head.next.next = head
    head.next = None # avoids cycle

    return new_head 
    