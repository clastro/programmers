def binary_search(low, high, target):
    """
    Perform a binary search to guess the target number.
    """
    while low <= high:
        mid = (low + high) // 2
        if mid == target:
            return mid
        elif mid < target:
            low = mid + 1
        else:
            high = mid - 1
    return None
