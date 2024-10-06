from typing import List


def radix_sort(arr: List[int]) -> None:
    """
    Sorts a list in ascending order using the radix sort algorithm.

    Args:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        None: The function sorts the list in place and does not return a value.

    Example:
        >>> nums = [1, 34, 21, 1, 5, 3, 54, 9]
        >>> radix_sort(nums)
        >>> print(nums)
        [1, 1, 3, 5, 9, 21, 34, 54]
    """

    maximum = max(arr)

    exp = 1

    while maximum // exp > 0:
        sort_by_digits(arr, exp)
        exp *= 10


def sort_by_digits(arr: List[int], exp: int) -> None:
    """
    Helper function to sort the array based on the current digit place.

    Args:
        arr (List[int]): The list of integers to be sorted by digit place.
        exp (int): The exponent corresponding to the digit place being sorted (1, 10, 100, etc.).

    Returns:
        None: The function sorts the list by the current digit place in place.
    """

    n = len(arr)
    result = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        result[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = result[i]


# Test array
array_one = [1, 34, 21, 1, 5, 3, 54, 9]

# Sort array
radix_sort(array_one)

# Print sorted array
print(array_one)
