from typing import List


def counting_sort(arr: List[int]) -> None:
    """
    Sorts a list in ascending order using the counting sort algorithm.

    Args:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        None: The function sorts the list in place and does not return a value.

    Example:
        >>> nums = [1, 34, 21, 1, 5, 3, 54, 9]
        >>> counting_sort(nums)
        >>> print(nums)
        [1, 1, 3, 5, 9, 21, 34, 54]
    """

    maximum = max(arr)
    minimum = min(arr)

    total_space = maximum - minimum + 1

    count = [0] * total_space

    for num in arr:
        count[num - minimum] += 1

    index = 0

    for i in range(total_space):
        while count[i] > 0:
            arr[index] = i + minimum
            index += 1
            count[i] -= 1


# Test array
array_one = [1, 34, 21, 1, 5, 3, 54, 9]

# Sort array
counting_sort(array_one)

# Print sorted array
print(array_one)
