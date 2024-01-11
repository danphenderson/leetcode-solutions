# [Problem](https://leetcode.com/problems/prison-cells-after-n-days/)

# Intuition
This problem illustrates a classic case of state manipulation in an 8-cell prison scenario. Given that there are $2^8=256$ possible states, the system is bound to repeat states, forming a cycle, especially for large values of n. Detecting this cycle is crucial to efficiently compute the prison's state at any given day.

While an abstract algebra perspective initially seemed promising, it was quickly deemed unsuitable. The permutation operation in our context does not satisfy certain group axioms, such as invertibility, since we cannot return to a state where the end cells are occupied.

# Approach
Setting aside abstract algebra, the problem initially appeared straightforward yet posed optimization challenges. My first brute-force method, without cycle detection, iteratively computed the next day's state, as shown below:

```python
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        def get_next_day(cells):
            # Compute the state for the next day
            return [0] + [1 if cells[i - 1] == cells[i + 1] else 0 for i in range(1, 7)] + [0]

        for day in range(n):
            cells = get_next_day(cells)
        
        return cells
```

However, this method did not leverage the cyclic nature of the problem. A critical realization was that the prison state repeats every 14 days. After the first iteration, the first and last cells remain vacant, reducing our problem to two separate 3-bit cycles among the middle six cells. This results in a maximum cycle length of 14 days.

We can optimize our solution significantly by considering this cyclical behavior. Reducing the number of days n modulo 14 allows us to efficiently compute the prison cells' state after n days, greatly reducing the computational complexity, particularly for large n values.

# Complexities
- Time Complexity: The worst-case time complexity is $O(1)$. This constant complexity arises because the number of iterations never exceeds 14, and each iteration involves constant time operations, regardless of the input size (n).
- Space Complexity: The space complexity is $O(1)$ as well, due to the use of a fixed-size array (the cells array of size 8) and a minimal number of variables for control and computation.

# Code

```python
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        
        n = (n % 14) if (n % 14) != 0 else 14
        
        for day in range(n):
            # Create a new state for the next day
            new_cells = [0] * 8
            for i in range(1, 7):
                new_cells[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            cells = new_cells

        return cells
```