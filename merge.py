from typing import List, Union


def merge_sort(arr: List[Union[int, float]]) -> None:
    """
    Sorts a list in ascending order using the merge sort algorithm.

    Args:
        arr (List[Union[int, float]]): The list of numbers (integers or floats) to be sorted.

    Returns:
        None: The function sorts the list in place and does not return a value.

    Example:
        >>> nums = [1, 34, 21, 1, 5, 3, 54, 9]
        >>> merge_sort(nums)
        >>> print(nums)
        [1, 1, 3, 5, 9, 21, 34, 54]
    """

    n = len(arr)

    if n > 1:
        mid = n // 2

        left_part = arr[:mid]
        right_part = arr[mid:]

        merge_sort(left_part)
        merge_sort(right_part)

        i = j = k = 0

        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1


# Test arrays
array_one = [1, 34, 21, 1, 5, 3, 54, 9]
array_two = [4.5, 3.7, 1.6, 0.4, 23.87]

# Sort arrays
merge_sort(array_one)
merge_sort(array_two)

# Print sorted arrays
print(array_one)
print(array_two)
