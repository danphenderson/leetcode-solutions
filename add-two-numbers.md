# [Problem](https://leetcode.com/problems/add-two-numbers/)

# Intuition

The key intuition behind this problem is understanding how numbers are added digit by digit from right to left, carrying any overflow to the next digit. We replicate this process using linked lists.

# Approach

The initial version, grown from the shell without any optimizations, is implemented using a deque to manage the summation process. This approach simulates the addition and manages the carry-over for each digit. However, this implementation is not the most efficient in terms of space and readability. 

```python
from collections import deque

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def create_list(values: list[int]):
            if not values:
                return None
            head = ListNode(values[0])
            current = head
            for value in values[1:]:
                current.next = ListNode(value)
                current = current.next
            return head

        # Early exit conditions
        if not l1 and not l2:
            return []
        if not l2:
            return create_list(l1)
        if not l1:
            return create_list(l2)

        # Building linked list as an array
        res = []
        stack = deque([[l1.val, l2.val]])
        

        while stack:
            digit_sum = sum(stack.pop())
            digit_sum_mod10 = digit_sum % 10
            res.append(digit_sum_mod10)
            next_digit_sum = []
            if digit_sum != digit_sum_mod10:
                next_digit_sum.append(1) # may fail?
            if l1.next:
                l1 = l1.next
                next_digit_sum.append(l1.val)
            if l2.next:
                l2 = l2.next
                next_digit_sum.append(l2.val)
            if next_digit_sum:
                stack.append(next_digit_sum)

        
        return create_list(res)
```
The inital approach beat $84%$ of other python users' runtime.


# Code

The optimized code simplifies the process by directly iterating through the linked lists, which improves readability and efficiency. The carry is handled more straightforwardly, and the overall structure is cleaner.


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = carry + x + y
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next
```

The optimized code beat $98.80%$ of other python users' runtime, as it provides a more streamlined and efficient approach to solving the problem, while maintaining the core logic of digit-by-digit addition with carry-over.

# Complexities
- Time Complexity: $O(max(N, M))$, where N and M are the lengths of the two linked lists. This is because we traverse each list once.
- Space Complexity: $O(max(N, M))$, as we store the result in a new linked list.