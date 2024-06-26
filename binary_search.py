def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage:
arr = [2, 3, 5, 7, 11, 13, 17, 19, 23]
target = 11
index = binary_search(arr, target)
print(f"Element {target} found at index {index}")  # Output: Element 11 found at index 4
