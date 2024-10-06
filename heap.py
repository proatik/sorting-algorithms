from typing import List, Union


def heap_sort(arr: List[Union[int, float]]) -> None:
    """
    Sorts a list in ascending order using the heap sort algorithm.

    Args:
        arr (List[Union[int, float]]): The list of numbers (integers or floats) to be sorted.

    Returns:
        None: The function sorts the list in place and does not return a value.

    Example:
        >>> nums = [1, 34, 21, 1, 5, 3, 54, 9]
        >>> heap_sort(nums)
        >>> print(nums)
        [1, 1, 3, 5, 9, 21, 34, 54]
    """

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def heapify(arr: List[Union[int, float]], n: int, i: int) -> None:
    """
    Turns a subtree rooted at index i into a max heap.

    Args:
        arr (List[Union[int, float]]): The list of numbers to heapify.
        n (int): The size of the heap.
        i (int): The index of the current root node.

    Returns:
        None: The function modifies the list in place.

    Example:
        >>> nums = [3, 1, 4, 1, 5, 9, 2]
        >>> heapify(nums, len(nums), 0)
    """

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Test arrays
array_one = [1, 34, 21, 1, 5, 3, 54, 9]
array_two = [4.5, 3.7, 1.6, 0.4, 23.87]

# Sort arrays
heap_sort(array_one)
heap_sort(array_two)

# Print sorted arrays
print(array_one)
print(array_two)
