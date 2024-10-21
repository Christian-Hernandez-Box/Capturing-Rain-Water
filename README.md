# Capturing Rain Water

This project contains two solutions for the "Capturing Rain Water" problem, which calculates the amount of water that can be trapped after raining given a list of non-negative integers representing an elevation map.

## Solutions

### Naive Solution

The naive solution iterates through each bar in the histogram and calculates the water trapped at that bar by finding the maximum height to the left and right of the bar. The amount of water trapped at the bar is the minimum of these two heights minus the height of the bar itself.

```python
def rain_water(histogram: List[int]) -> int:
    total_water = 0

    for i in range(1, len(histogram) - 1):
        left_max = max(histogram[:i])
        right_max = max(histogram[i + 1:])
        fill_mark = min(left_max, right_max)
        water_at_index = fill_mark - histogram[i]
        if water_at_index > 0:
            total_water += water_at_index

    return total_water
```

### Optimized Solution

The optimized solution improves on the naive solution by precomputing the maximum heights to the left and right of each bar in two passes. This allows the water trapped at each bar to be calculated in constant time.

```python
def optimized_rain_water(histogram: List[int]) -> int:
    if not histogram:
        return 0

    n = len(histogram)
    left_maxes = [0] * n
    right_maxes = [0] * n

    # Calculate left maxes
    left_maxes[0] = histogram[0]
    for i in range(1, n):
        left_maxes[i] = max(left_maxes[i - 1], histogram[i])

    # Calculate right maxes
    right_maxes[-1] = histogram[-1]
    for i in range(n - 2, -1, -1):
        right_maxes[i] = max(right_maxes[i + 1], histogram[i])

    # Calculate total water
    total = 0
    for i in range(n):
        fill_mark = min(left_maxes[i], right_maxes[i])
        water_at_index = fill_mark - histogram[i]
        if water_at_index > 0:
            total += water_at_index

    return total
```

## Test Inputs

The file includes some test inputs to verify the solutions:

```python
small = [1, 0, 1]
medium = [4, 2, 1, 3, 0, 1, 2]
edge_case = [0, 2, 0]
```

## Usage

To use the solutions, simply call the `rain_water` or `optimized_rain_water` functions with a list of integers representing the elevation map.

```python
print(rain_water(small))  # Output: 1
print(optimized_rain_water(medium))  # Output: 6
```

## License

This project is licensed under the MIT License.
