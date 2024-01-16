def linear_search(elements, value) -> int:
    """Returns the index of the value in elements if present, otherwise -1."""
    for ind, element in enumerate(elements):
        if element == value:
            return ind
    return -1

def binary_search(elements, value) -> int:
    """Returns the index of the value in elements if present, otherwise -1.
    
    Binary Search algorithm is used on a sorted array by repeatedly dividing the
    search interval in half. The idea of binary search is to use the information
    that the array is sorted and reduce the time complexity to O(log N).
    """
    size = len(elements)
    lp = 0
    rp = size - 1

    while lp <= rp:
        mp = (lp + rp) // 2

        if elements[mp] == value:
            return mp                

        elif elements[mp] < value:
            lp = mp + 1
        else: 
            rp = mp - 1

    return -1


def binary_search_recursive(elements, value) -> int:
    """Returns the index of the value in elements if present, otherwise -1."""

    def _binary_search_recursive(elements, lp, rp, value):
        if rp < lp:                     # early exit if element is not in arry
            return -1
        mp = (lp + rp) // 2
        if elements[mp] == value:       # element is present at mp
            return mp
        elif elements[mp] < value:      # element is to the right of mp
            return _binary_search_recursive(elements, mp + 1, rp, value)
        else:                           # element is to the left of mp 
            return _binary_search_recursive(elements, lp, mp - 1, value)
        
    return _binary_search_recursive(elements, 0, len(elements) - 1, value)