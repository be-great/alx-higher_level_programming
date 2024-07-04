#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    def binary_search_peak(arr, low, high):
        """Use binary search to find a peak."""
        mid = low + (high - low) // 2
        
        # Check if the mid  is a peak
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (
                mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
            return arr[mid]

        elif mid > 0 and arr[mid - 1] > arr[mid]:
            return binary_search_peak(arr, low, mid - 1)

        else:
            return binary_search_peak(arr, mid + 1, high)

    if not list_of_integers:
        return None

    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)
