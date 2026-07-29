import time

# Insertion Sort Function
def insertion_sort(arr):
    n = len(arr)

    # Insertion Sort Algorithm
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key at its correct position
        arr[j + 1] = key

    return arr


# -------------------- Main Program --------------------

# User Input
size = int(input("Enter the number of elements in the array: "))

arr = []
print("Enter the elements:")
for i in range(size):
    arr.append(int(input(f"Element {i + 1}: ")))

print("\nOriginal Array:", arr)

# Measure Execution Time
start_time = time.perf_counter()

sorted_array = insertion_sort(arr)

end_time = time.perf_counter()

# Display Results
print("\nSorted Array:", sorted_array)
print(f"Execution Time: {(end_time - start_time):.10f} seconds")

# Time Complexity Information
print("\nTime Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")

# Space Complexity
print("\nSpace Complexity: O(1)")
import time

# Linear Search Function
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Binary Search Function
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# User Input
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))

print("\nChoose Search Method")
print("1. Linear Search")
print("2. Binary Search")
choice = int(input("Enter your choice (1 or 2): "))

# Perform Search
if choice == 1:
    start_time = time.perf_counter()

    result = linear_search(arr, key)

    end_time = time.perf_counter()

    print("\n--- Linear Search Result ---")
    if result != -1:
        print(f"Element {key} found at index {result}.")
    else:
        print(f"Element {key} not found.")

    print("\nTime Complexity:")
    print("Best Case    : O(1)")
    print("Average Case : O(n)")
    print("Worst Case   : O(n)")

elif choice == 2:
    arr.sort()
    print("\nSorted Array:", arr)

    start_time = time.perf_counter()

    result = binary_search(arr, key)

    end_time = time.perf_counter()

    print("\n--- Binary Search Result ---")
    if result != -1:
        print(f"Element {key} found at index {result} in the sorted array.")
    else:
        print(f"Element {key} not found.")

    print("\nTime Complexity:")
    print("Best Case    : O(1)")
    print("Average Case : O(log n)")
    print("Worst Case   : O(log n)")

else:
    print("Invalid choice!")
    exit()

# Display Execution Time
execution_time = end_time - start_time
print(f"\nExecution Time: {execution_time:.10f} seconds")
import time

# Selection Sort Function
def selection_sort(arr):
    n = len(arr)

    # Selection Sort Algorithm
    for i in range(n):
        min_index = i

        # Find the index of the smallest element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# -------------------- Main Program --------------------

# User Input
size = int(input("Enter the number of elements in the array: "))

arr = []
print("Enter the elements:")
for i in range(size):
    arr.append(int(input(f"Element {i + 1}: ")))

print("\nOriginal Array:", arr)

# Measure Execution Time
start_time = time.perf_counter()

sorted_array = selection_sort(arr)

end_time = time.perf_counter()

# Display Results
print("\nSorted Array:", sorted_array)
print(f"Execution Time: {(end_time - start_time):.10f} seconds")

# Time Complexity Information
print("\nTime Complexity:")
print("Best Case    : O(n²)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")

# Space Complexity
print("\nSpace Complexity: O(1)")
import time

# Selection Sort Function
def selection_sort(arr):
    n = len(arr)

    # Selection Sort Algorithm
    for i in range(n):
        min_index = i

        # Find the index of the smallest element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# -------------------- Main Program --------------------

# User Input
size = int(input("Enter the number of elements in the array: "))

arr = []
print("Enter the elements:")
for i in range(size):
    arr.append(int(input(f"Element {i + 1}: ")))

print("\nOriginal Array:", arr)

# Measure Execution Time
start_time = time.perf_counter()

sorted_array = selection_sort(arr)

end_time = time.perf_counter()

# Display Results
print("\nSorted Array:", sorted_array)
print(f"Execution Time: {(end_time - start_time):.10f} seconds")

# Time Complexity Information
print("\nTime Complexity:")
print("Best Case    : O(n²)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")

# Space Complexity
print("\nSpace Complexity: O(1)")
import time

# Selection Sort Function
def selection_sort(arr):
    n = len(arr)

    # Selection Sort Algorithm
    for i in range(n):
        min_index = i

        # Find the index of the smallest element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# -------------------- Main Program --------------------

# User Input
size = int(input("Enter the number of elements in the array: "))

arr = []
print("Enter the elements:")
for i in range(size):
    arr.append(int(input(f"Element {i + 1}: ")))

print("\nOriginal Array:", arr)

# Measure Execution Time
start_time = time.perf_counter()

sorted_array = selection_sort(arr)

end_time = time.perf_counter()

# Display Results
print("\nSorted Array:", sorted_array)
print(f"Execution Time: {(end_time - start_time):.10f} seconds")

# Time Complexity Information
print("\nTime Complexity:")
print("Best Case    : O(n²)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")

# Space Complexity
print("\nSpace Complexity: O(1)")