# Sorting Algorithms

This document provides a summary of the key points for various sorting algorithms implemented in Python. It is designed to be a quick reference guide for revising the characteristics of each algorithm. Below, you will find links to the respective Python files containing the implementations, along with bullet points highlighting their key features.

```
01. Bubble Sort
02. Selection Sort
03. Insertion Sort
04. Merge Sort
05. Quick Sort
06. Cycle Sort
07. Heap Sort
08. Counting Sort
09. Radix Sort
10. Bucket Sort
11. Shell Sort
```

## 01. Bubble Sort

- **Stable**: Yes
- **In-place**: Yes
- **Time Complexity**: Best: O(n), Average and Worst: O(n²)
- **Space Complexity**: O(1)
- **Use Case**: Simple to implement, primarily educational, not efficient for large datasets.
- **Algorithm Type**: Comparison-based
- **Adaptiveness**: Adaptive (can detect if already sorted)
- **Number of Swaps/Comparisons**: High number of swaps, performs n(n-1)/2 comparisons in the worst case.

[View Bubble Sort Implementation](./bubble.py)

## 02. Selection Sort

- **Stable**: No
- **In-place**: Yes
- **Time Complexity**: Best, Average, and Worst: O(n²)
- **Space Complexity**: O(1)
- **Use Case**: Simple to implement, sometimes used when memory writes are costly.
- **Algorithm Type**: Comparison-based
- **Adaptiveness**: Non-adaptive
- **Number of Swaps/Comparisons**: Minimizes the number of swaps; performs n(n-1)/2 comparisons.

[View Selection Sort Implementation](./selection.py)

## 03. Insertion Sort

- **Stable**: Yes
- **In-place**: Yes
- **Time Complexity**: Best: O(n), Average and Worst: O(n²)
- **Space Complexity**: O(1)
- **Use Case**: Faster for small lists, adaptive on nearly sorted data.
- **Algorithm Type**: Comparison-based
- **Adaptiveness**: Adaptive (efficient on partially sorted arrays)
- **Number of Swaps/Comparisons**: Performs fewer swaps; performs n(n-1)/2 comparisons in the worst case.

[View Insertion Sort Implementation](./insertion.py)

## 04. Merge Sort

- **Stable**: Yes
- **In-place**: No (Requires O(n) additional space)
- **Time Complexity**: Best, Average, and Worst: O(n log n)
- **Space Complexity**: O(n)
- **Use Case**: Efficient for large data sets, stable sorting.
- **Algorithm Type**: Divide and Conquer
- **Adaptiveness**: Non-adaptive
- **Number of Swaps/Comparisons**: Performs O(n log n) comparisons.

[View Merge Sort Implementation](./merge.py)

## 05. Quick Sort

- **Stable**: No
- **In-place**: Yes
- **Time Complexity**: Best and Average: O(n log n), Worst: O(n²)
- **Space Complexity**: O(log n) (due to recursion stack)
- **Use Case**: Efficient for large datasets, often used in practice due to good average performance.
- **Algorithm Type**: Divide and Conquer
- **Adaptiveness**: Non-adaptive
- **Number of Swaps/Comparisons**: Performs fewer swaps; O(n log n) comparisons on average.

[View Quick Sort Implementation](./quick.py)

## 06. Cycle Sort

- **Stable**: No
- **In-place**: Yes
- **Time Complexity**: Best, Average, and Worst: O(n²)
- **Space Complexity**: O(1)
- **Use Case**: Minimizes memory writes, ideal for scenarios where write operations are costly.
- **Algorithm Type**: In-place sorting
- **Adaptiveness**: Non-adaptive
- **Number of Swaps/Comparisons**: Minimizes the number of swaps, O(n) writes

[View Cycle Sort Implementation](./cycle.py)

## 07. Heap Sort

- **Stable**: No
- **In-place**: Yes
- **Time Complexity**: Best, Average, and Worst: O(n log n)
- **Space Complexity**: O(1)
- **Use Case**: Efficient for large datasets, used in systems where consistent performance is required.
- **Algorithm Type**: Comparison-based, heap data structure
- **Adaptiveness**: Non-adaptive
- **Number of Swaps/Comparisons**: O(n log n) comparisons, fewer swaps compared to some algorithms

[View Heap Sort Implementation](./heap.py)

## 08. Counting Sort

- **Stable**: Yes
- **In-place**: No (requires additional space for the counting array)
- **Time Complexity**: Best, Average, and Worst: O(n + k)
- **Space Complexity**: O(n + k)
- **Use Case**: Suitable for sorting integers with a known, limited range.
- **Algorithm Type**: Non-comparison-based
- **Adaptiveness**: Non-adaptive
- **Number of Swaps/Comparisons**: Does not perform swaps, but uses O(n + k) comparisons

[View Counting Sort Implementation](./counting.py)

## 09. Radix Sort

- **Stable**: Yes
- **In-place**: No (requires additional space for the output array)
- **Time Complexity**: Best, Average, and Worst: O(d \* (n + k)) where d is the number of digits, n is the size of the input array, and k is the range of digits (usually 10)
- **Space Complexity**: O(n + k)
- **Use Case**: Suitable for sorting large sets of integers where the range of digits is limited.
- **Algorithm Type**: Non-comparison-based
- **Adaptiveness**: Non-adaptive
- **Number of Swaps/Comparisons**: Does not perform traditional swaps, but performs O(n) operations per digit

[View Radix Sort Implementation](./radix.py)

## 10. Bucket Sort

- **Stable**: Yes (depending on the sorting algorithm used in individual buckets)
- **In-place**: No (requires additional space for the buckets)
- **Time Complexity**: Best: O(n + k), Average: O(n + k), Worst: O(n²) (when all elements fall into the same bucket)
- **Space Complexity**: O(n + k) (space for buckets)
- **Use Case**: Suitable for sorting positive floating-point numbers uniformly distributed over a range (e.g., [0, 1)).
- **Algorithm Type**: Non-comparison-based
- **Adaptiveness**: Non-adaptive
- **Number of Swaps/Comparisons**: Comparisons depend on the sorting algorithm used within buckets

[View Bucket Sort Implementation](./bucket.py)

## 11. Shell Sort

- **Stable**: No
- **In-place**: Yes
- **Time Complexity**: Best: O(n log n), Average: O(n^(3/2)), Worst: O(n²)
- **Space Complexity**: O(1)
- **Use Case**: Useful for medium-sized datasets, and faster than Insertion Sort on average. Good for scenarios where simple implementation and improved time complexity over quadratic sorts is needed.
- **Algorithm Type**: Comparison-based
- **Adaptiveness**: Non-adaptive
- **Number of Swaps/Comparisons**: More comparisons and swaps in early stages with larger gaps; fewer in later stages

[View Shell Sort Implementation](./shell.py)
