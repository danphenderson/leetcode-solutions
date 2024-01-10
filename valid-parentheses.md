# [Problem](https://leetcode.com/problems/valid-parentheses/description/)

# Intuition
The problem of validating parentheses is based on the principle of matching pairs - every opening bracket must be closed by the same type of bracket, and in the correct order. This naturally suggests the use of a stack, a data structure that follows the Last-In, First-Out (LIFO) principle.

# Complexities
- Time Complexity: $O(n)$, where $n$ is the length of the input string.
- Space Complexity: $O(n)$, where $n$ is the length of the input string.

# Code
```python
class Solution:
    def isValid(self, s: str) -> bool:
        # A mapping of closing brackets to their corresponding opening brackets
        bracket_map = {
            ")": "(", "}" : "{", "]" : "[",
        }

        # Initialize a stack
        stack = []

        # Iterate through each character in the string
        for char in s:
            if char in bracket_map:
                # Pop the top element from the stack if it is not empty, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'

                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket by assumption and we push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly
        return not stack
```