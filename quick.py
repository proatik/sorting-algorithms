from typing import List, Union


def quick_sort(arr: List[Union[int, float]]) -> None:
    """
    Sorts a list in ascending order using the quick sort algorithm.

    Args:
        arr (List[Union[int, float]]): The list of numbers (integers or floats) to be sorted.

    Returns:
        None: The function sorts the list in place and does not return a value.

    Example:
        >>> nums = [1, 34, 21, 1, 5, 3, 54, 9]
        >>> quick_sort(nums)
        >>> print(nums)
        [1, 1, 3, 5, 9, 21, 34, 54]
    """

    perform_quick_sort(arr, 0, len(arr) - 1)


def perform_quick_sort(arr: List[Union[int, float]], low: int, high: int) -> None:
    """
    Recursively sorts the sub-array using the quick sort algorithm.

    Args:
        arr (List[Union[int, float]]): The list of elements to be sorted.
        low (int): The starting index of the sub-array to be sorted.
        high (int): The ending index of the sub-array to be sorted.
    """

    if low < high:
        pivot_index = partition_by_pivot(arr, low, high)
        perform_quick_sort(arr, low, pivot_index - 1)
        perform_quick_sort(arr, pivot_index + 1, high)


def partition_by_pivot(arr: List[Union[int, float]], low: int, high: int) -> int:
    """
    Partitions the array around a pivot element and returns the pivot index.

    Args:
        arr (List[Union[int, float]]): The list of elements to be partitioned.
        low (int): The starting index of the sub-array to be partitioned.
        high (int): The ending index of the sub-array to be partitioned.

    Returns:
        int: The index of the pivot element after partitioning.
    """

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# Test arrays
array_one = [1, 34, 21, 1, 5, 3, 54, 9]
array_two = [4.5, 3.7, 1.6, 0.4, 23.87]

# Sort arrays
quick_sort(array_one)
quick_sort(array_two)

# Print sorted arrays
print(array_one)
print(array_two)
