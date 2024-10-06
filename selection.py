from typing import List, Union


def selection_sort(arr: List[Union[int, float]]) -> None:
    """
    Sorts a list in ascending order using the selection sort algorithm.

    Args:
        arr (List[Union[int, float]]): The list of numbers (integers or floats) to be sorted.

    Returns:
        None: The function sorts the list in place and does not return a value.

    Example:
        >>> nums = [1, 34, 21, 1, 5, 3, 54, 9]
        >>> selection_sort(nums)
        >>> print(nums)
        [1, 1, 3, 5, 9, 21, 34, 54]
    """

    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


# Test arrays
array_one = [1, 34, 21, 1, 5, 3, 54, 9]
array_two = [4.5, 3.7, 1.6, 0.4, 23.87]

# Sort arrays
selection_sort(array_one)
selection_sort(array_two)

# Print sorted arrays
print(array_one)
print(array_two)
