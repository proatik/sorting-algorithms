from typing import List, Union


def cycle_sort(arr: List[Union[int, float]]) -> None:
    """
    Sorts a list in ascending order using the cycle sort algorithm.

    Args:
        arr (List[Union[int, float]]): The list of numbers (integers or floats) to be sorted.

    Returns:
        None: The function sorts the list in place and does not return a value.

    Example:
        >>> nums = [1, 34, 21, 1, 5, 3, 54, 9]
        >>> cycle_sort(nums)
        >>> print(nums)
        [1, 1, 3, 5, 9, 21, 34, 54]
    """

    n = len(arr)

    for start in range(n - 1):
        item = arr[start]
        pos = start

        for i in range(start + 1, n):
            if arr[i] < item:
                pos += 1

        if pos == start:
            continue

        while item == arr[pos]:
            pos += 1

        arr[pos], item = item, arr[pos]

        while pos != start:
            pos = start

            for i in range(start + 1, n):
                if arr[i] < item:
                    pos += 1

            while item == arr[pos]:
                pos += 1

            arr[pos], item = item, arr[pos]


# Test arrays
array_one = [1, 34, 21, 1, 5, 3, 54, 9]
array_two = [4.5, 3.7, 1.6, 0.4, 23.87]

# Sort arrays
cycle_sort(array_one)
cycle_sort(array_two)

# Print sorted arrays
print(array_one)
print(array_two)
