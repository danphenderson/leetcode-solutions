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

def merge_sort(elements:list) -> list:
    ...

def quick_sort(elements:list) -> list:
    ...
