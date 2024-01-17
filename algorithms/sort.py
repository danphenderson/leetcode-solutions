def bubble_sort(elements:list) -> list:
    """O(N^2) runtime"""
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[i] > elements[i+1]: # then swap
                tmp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = tmp
                swapped = True
        if not swapped:
            break
    return elements

def insertion_sort(elements:list) -> list:
    ...


def merge(left: list, right:list):
    """Merge two sorted lists into a single sorted list."""
    merged = []
    i = j = 0

    # Traverse both lists and insert smaller of both elements in 'merged'
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Once we run out of elements in either list, append the remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged    


def merge_sort(elements:list) -> list:
    """O(N*logN) runtime. Divide and conquer problem."""
    size = len(elements)

    # Base Case: an array of zero or one elements is sorted, by definition
    if size < 2:
        return elements
    
    # Recursive Step
    left = merge_sort(elements[:size//2])
    right = merge_sort(elements[size//2:])
    
    # Merge the now-sorted sublists
    return merge(left, right)


def quick_sort(elements:list) -> list:
    ...
