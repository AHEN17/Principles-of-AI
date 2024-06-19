def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

# Example usage:
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
target_number = int(input("Enter the number to search for: "))
index = linear_search(numbers, target_number)
if index != -1:
    print(f"Number {target_number} found at index {index}.")
else:
    print(f"Number {target_number} not found in the list.")
