# Sorting Algorithms

## Quick Sort

The dreaded "divide and conquer" sort with the pivot. The idea is to select a smart pivot value and move every value <= the pivot to the left side of the list and every value > the pivot to its right side. The pivot is then in its final sorted position. Repeat this algorithm recursively on both sides of the list (minus the original pivot) until you cannot divide the list anymore. If performed correctly, the original list will be sorted in-place.

Average case: O(n log n)
Best case: O(n log n)
Worst case: O(n<sup>2</sup>)

In-place: Usually.
Stable: Usually not.

The worst case occurs if after every single partition, the list (length n) becomes divided into lengths 1 and and (n - 1). This is why a smart pivot selection algorithm, like median-of-three, is crucial for performance.


## Merge Sort

Another "divide and conquer" sort. Divide the array into the smallest chunks possible before sorting (lists of one), then, recombine adjacent lists recursively sorting the two while doing so. When there's a single array left, the list is sorted.

All cases: O(n log n)

In-place: Usually not.
Stable: Usually.

Note that this one usually requires extra memory since the in-place variation is not common.
