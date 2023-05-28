def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Get user input
input_str = input("Enter a list of numbers separated by spaces: ")

# Convert input string to a list of integers
numbers = [int(x) for x in input_str.split()]

# Sort the numbers using selection sort
sorted_numbers = selection_sort(numbers)

# Print the sorted numbers
print("Sorted numbers:", sorted_numbers)