# The Big-O Cheatsheet

## Sorting Algorithms

### Quick Sort

The dreaded "divide and conquer" sort with the pivot. The idea is to select a smart pivot value and move every value <= the pivot to the left side of the list and every value > the pivot to its right side. The pivot is then in its final sorted position. Repeat this algorithm recursively on both sides of the list (minus the original pivot) until you cannot divide the list anymore. If performed correctly, the original list will be sorted in-place.

Average case: O(n log n)
Best case: O(n log n)
Worst case: O(n<sup>2</sup>)

In-place: Usually.
Stable: Usually not.

The worst case occurs if after every single partition, the list (length n) becomes divided into lengths 1 and and (n - 1). This is why a smart pivot selection algorithm, like median-of-three, is crucial for performance.


### Merge Sort

Another "divide and conquer" sort. This time we divide the array into the smallest chunks possible before sorting.

Recursively break the array down into chunks of size 1.

All cases: O(n log n)

In-place: Usually not.
Stable: Usually.


### Heap Sort

Average case:
Best case:
Worst case:

In-place: Yes.
Stable: No.


### Selection Sort

The simplest sort to understand. Starting at position (index) 0, for each remaining entry in the list, sequentially search for the smallest value. Swap its value at your current position with the the minimum value. Repeat for every position.

All cases: O(n<sup>2</sup>)

Stable: Yes. (If you use < instead of <=)


### Insertion Sort

Average case:
Best case:
Worst case:

Memory usage:


## Searching Algorithms

### Binary Search


### Breadth First Search

A "breadth" first search will


### Depth First Search
