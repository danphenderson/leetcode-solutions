# [Problem](https://leetcode.com/problems/merge-two-sorted-lists/description/)

# Intuition
We can merge two sorted lists by comparing the values of the two lists at each step and appending the smaller value to the merged list. This process is repeated until one of the lists is exhausted, at which point the remaining elements of the other list are appended to the merged list.

This is an excercise in basic pointer manipulation.

# Complexities
- Time Complexity: $$O(n + m)$$, where $$n$$ and $$m$$ are the lengths of the two input lists.
- Space Complexity: $$O(1)$$, constant space is used.

# Code
```python
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create the head node to act as the starting point of the merged list
        dummy = ListNode()
        
        tail = dummy

        # Traverse through both lists
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Append the remaining elements of list1 or list2
        tail.next = list1 if list1 else list2

        # Return the next node of the dummy node, which is the head of the merged list
        return dummy.next
```