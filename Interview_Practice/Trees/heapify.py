def heapify(arr, n, i):
    smallest = i  # Assume current node is smallest
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # Swap
        heapify(arr, n, smallest)  # Recursively heapify

def build_min_heap(arr):
    n = len(arr)
    # Start from last non-leaf node and heapify each
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# Example usage
arr = [5, 3, 8, 1, 2, 9]
build_min_heap(arr)
print(arr)  # Should be a valid min heap