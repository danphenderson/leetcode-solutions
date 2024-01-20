# [Problem](https://leetcode.com/problems/sum-of-subarray-minimums)


# Approach
To solve this problem efficiently, we can use a stack-based approach. The idea is to find, for each element in the array, the distance to the next smaller element and the distance to the previous smaller element. This way, we can calculate how many subarrays where this element is the minimum.

Here's a step-by-step approach:

1. Initialization: We initialize a stack to keep track of elements and their indices, and two arrays (left, right) to store the distance to the next and previous smaller elements.

2. Iterating through the Array: For each element in the array, we pop from the stack until the top of the stack is less than the current element. This process will give us the index of the previous smaller element.

3. Calculating Distances: For the current element at index i, the distance to the previous smaller element is i - stack[-1], and the distance to the next smaller element is calculated in a similar way.

4. Calculating the Sum: The contribution of the current element to the final sum is its value multiplied by the product of these distances. This is because it's the minimum in exactly that many subarrays.

5. Handling the Stack: After processing each element, push its index onto the stack.

6. Modulo Operation: Since the answer can be large, take modulo 10^9 + 7 at each step to prevent integer overflow.


# Complexities
- Time Complexity: $O(n)$, where $n$ is the length of `arr`, because each element is pushed and popped from the stak at most once.
- Space Complexity: $O(n)$, for the stack and the two auxillary arrays `left` and `write`.

# Code

```python
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        left, right = [0] * n, [0] * n
        stack = []

        # Left
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = i + 1 if not stack else i - stack[-1]
            stack.append(i)

        # Clear the stack for the right pass
        stack.clear()

        # Right
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = n - i if not stack else stack[-1] - i
            stack.append(i)

        # Calculate the answer
        return sum(a * l * r for a, l, r in zip(arr, left, right)) % MOD
```