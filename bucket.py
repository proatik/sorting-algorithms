from typing import List


def bucket_sort(arr: List[float]) -> None:
    """
    Sorts an array of positive floating-point numbers using the bucket sort algorithm.

    Args:
        arr (List[float]): The list of floating-point numbers to be sorted.

    Returns:
        None: The function sorts the list in place and does not return a value.

    Example:
        >>> nums = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47]
        >>> bucket_sort(nums)
        >>> print(nums)
        [0.23, 0.25, 0.32, 0.42, 0.47, 0.52]
    """

    n = len(arr)

    if n <= 1:
        return

    buckets = [[] for _ in range(n)]

    for num in arr:
        index = int(num * n)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1


# Test array
array_two = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47]

# Sort array
bucket_sort(array_two)

# Print sorted array
print(array_two)
