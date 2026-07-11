# Coding my favorite sorting algorithm, Merge Sort, in Python
"""
How does Merge Sort work? Merge Sort is a divide and conquer algorithm that
divides the input array into two halves, recursively sorts each half, and
then merges the sorted halves back together. The process continues until
the entire array is sorted.

The reason I love mergesort is because it perfectly symbolizes how the
human mind approaches complex problems: by breaking down something unclear
and chaotic into its simplest, ordered parts.

Before we define merge_sort, we need a helper function called merge. The
merge function takes two sorted arrays and combines them into a single
sorted array, by comparing elements from both arrays and adding the
smaller one to the result until everything has been added.
"""

def merge(left, right):
    merged = []
    i, j = 0, 0

    # Compare elements from both arrays and add the smaller one first
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add whatever is left over, since one array may still have elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


"""
Let's break down the steps of Merge Sort!
"""

def merge_sort(arr):
    # Base case: an array with one or zero elements is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2

    # Recursively sort each half. Each call keeps splitting the array
    # until we hit the base case, then the recursion unwinds and the
    # sorted halves get merged back together
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the two sorted halves into one sorted array
    return merge(left_half, right_half)


"""
Let's test our merge_sort function with an example array. We create an
unsorted array, pass it to merge_sort, and print the result to confirm
it worked.
"""

if __name__ == "__main__":
    array_unsorted = [1, 3, 10, 6, 8, 0, 0, 8, 8, 42, 41, 32, -9]
    array_sorted = merge_sort(array_unsorted)
    print("Unsorted array:", array_unsorted)
    print("Sorted array:", array_sorted)
