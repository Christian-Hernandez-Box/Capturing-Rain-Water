from typing import List

####### TEST INPUTS HERE
small = [1, 0, 1]
medium = [4, 2, 1, 3, 0, 1, 2]
edge_case = [0, 2, 0]

####### NAIVE SOLUTION HERE
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

####### OPTIMIZED SOLUTION HERE
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