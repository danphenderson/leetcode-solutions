# [Problem](https://leetcode.com/problems/pascals-triangle/description/)

# Intuition
Pascal's triangle is a classic example of a problem that can be elegantly solved using a dynamic programming approach. Each entry in Pascal's triangle is the sum of the two entries directly above it, with the exception of the edges of the triangle, which are always 1. This problem requires an understanding of how to construct each row based on the previous one, recognizing that the first and last elements of each row are always 1, and intermediate elements are sums of two adjacent elements from the preceding row.

# Approach
The algorithm starts by handling the base case of `numRows == 0`. For all other cases, it initializes the triangle with the first row `[1]`. The approach then iteratively constructs each subsequent row of Pascal's triangle based on the following rules:

1. **Initialization of Each Row**: Each row starts with a `1`.
2. **Intermediate Values**: Each intermediate value in a row is computed as the sum of the two numbers directly above it in the triangle. This is achieved by adding the elements at the same position and the position before it in the previous row.
3. **Finalizing Each Row**: Each row ends with a `1`. After computing the intermediate values, a `1` is appended to the row to complete it.
4. **Building the Triangle**: Each completed row is added to the triangle, gradually building up Pascal's triangle row by row until the desired numRows is reached.


# Complexity
Time Complexity: $O(n^2)$, where $n$ is numRows. The time complexity arises from the nested loops: the outer loop runs for numRows iterations, and the inner loop's runtime is proportional to the row number, summing up to a quadratic time complexity. 
Space Complexity: $O(n^2)$ as the space required is proportional to the number of elements in Pascal's triangle, which is the sum of the first n natural numbers, resulting in a quadratic relationship with the number of rows. The space complexity considers the storage required for the triangle structure itself, which holds all the computed values.

# Code
My solution beats 97-percent of Python submissions' runtime.

```python
def generate(self, numRows: int) -> List[List[int]]:
    if numRows == 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for row_num in range(1, numRows):
        # Start the row with 1
        row = [1]

        # Calculate the intermediate values of the row
        for i in range(1, row_num):
            row.append(triangle[row_num - 1][i - 1] + triangle[row_num - 1][i])

        # End the row with 1
        row.append(1)

        # Add the completed row to the triangle
        triangle.append(row)

    return triangle
```