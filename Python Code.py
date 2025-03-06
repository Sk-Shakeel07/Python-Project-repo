# Searching and Sorting Algorithms

def linear_search(arr, target):
    """
    Perform linear search on a list.
    Time Complexity: O(n)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index of the target element
    return -1  # Return -1 if target is not found

def binary_search(arr, target):
    """
    Perform binary search on a sorted list.
    Time Complexity: O(log n)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2  # Prevents overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def bubble_sort(arr):
    """
    Perform Bubble Sort.
    Time Complexity: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Optimization: Stops if already sorted
    return arr

def insertion_sort(arr):
    """
    Perform Insertion Sort.
    Time Complexity: O(n^2)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    """
    Perform Selection Sort.
    Time Complexity: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort(arr):
    """
    Perform Merge Sort.
    Time Complexity: O(n log n)
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """Helper function to merge two sorted lists."""
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def quick_sort(arr):
    """
    Perform Quick Sort.
    Time Complexity: O(n log n) on average, O(n^2) in worst case.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Test cases
if __name__ == "__main__":
    test_list = [64, 34, 25, 12, 22, 11, 90]
    
    print("Linear Search:", linear_search(test_list, 22))
    test_list_sorted = sorted(test_list)
    print("Binary Search:", binary_search(test_list_sorted, 22))
    
    print("Bubble Sort:", bubble_sort(test_list.copy()))
    print("Insertion Sort:", insertion_sort(test_list.copy()))
    print("Selection Sort:", selection_sort(test_list.copy()))
    print("Merge Sort:", merge_sort(test_list.copy()))
    print("Quick Sort:", quick_sort(test_list.copy()))
