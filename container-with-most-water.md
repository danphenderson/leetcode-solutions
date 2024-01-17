# [Problem](https://leetcode.com/problems/container-with-most-water/description/)

# Intuition
The problem "Container With Most Water" asks us to find the maximum amount of water that can be contained within a set of vertical lines, represented by an array where each element signifies the height of a line. The width between any two lines is determined by their indices in the array.

The intuitive approach to this problem is to consider every possible pair of lines and calculate the area of the water container they form. However, this brute-force approach is inefficient as it results in a quadratic time complexity. A more efficient solution involves a two-pointer approach, starting with the widest possible container and gradually moving the pointers inward to find a potentially larger container.

# Approach

1. Initialization: Start with two pointers, one at the beginning (`lp`) and one at the end (`rp`) of the array. This setup gives us the widest possible container initially.
2. Iterate and Calculate Area: While `lp` is less than `rp`:
    - Calculate the `area` formed between the lines at `lp` and `rp`. The area is determined by the shorter line (since it determines the height of the water) and the distance between the two lines.
    - Update `max_area` if the calculated area is larger than the current `max_area`.
    - Move the pointer at the shorter line inward (increment `lp` if the left line is shorter, or decrement `rp` if the right line is shorter). This step is crucial as moving the taller line inward would not help in finding a larger area.
3. Return Result: Once the pointers meet, return the `max_area`.

# Complexities
- Time Complexity: The algorithm involves a single pass through the array with two pointers moving towards each other. Therefore, the time complexity is $O(n)$, where $n$ is the number of elements in the array.
- Space Complexity: The solution only uses a constant amount of extra space for variables like `lp`, `rp`, `area`, and `max_area`. Hence, the space complexity is $O(1)$.


# Code
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        lp, rp = 0, n - 1
        area = max_area = 0
        while lp < rp:
            area = min(height[lp], height[rp]) * (rp - lp)
            max_area = max(area, max_area)
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
        return max_area          
```