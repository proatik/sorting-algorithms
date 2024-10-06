from typing import List, Union


def bubble_sort(arr: List[Union[int, float]]) -> None:
    """
    Sorts a list in ascending order using the bubble sort algorithm.

    Args:
        arr (List[Union[int, float]]): The list of numbers (integers or floats) to be sorted.

    Returns:
        None: The function sorts the list in place and does not return a value.

    Example:
        >>> nums = [1, 34, 21, 1, 5, 3, 54, 9]
        >>> bubble_sort(nums)
        >>> print(nums)
        [1, 1, 3, 5, 9, 21, 34, 54]
    """

    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]

        if not swapped:
            break


# Test arrays
array_one = [1, 34, 21, 1, 5, 3, 54, 9]
array_two = [4.5, 3.7, 1.6, 0.4, 23.87]

# Sort arrays
bubble_sort(array_one)
bubble_sort(array_two)

# Print sorted arrays
print(array_one)
print(array_two)
