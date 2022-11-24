# Binary Search Algorithm
def binary_search(array , n):
    low = 0
    high = len(array)-1
    
    while (low <= high):
        mid = low + (high - low)//2
        if (array[mid] == n):
            return mid
        elif (array[mid] < n):
            low = mid + 1
        else:
            high = mid - 1
    return -1


array = [2 , 5 , 4 , 7 , 6]
n = 7
result = binary_search(array , n)

if result == -1:
  print("Element not found")
else:
  print("Element is found at index ", result)

# Time Complexity ---> O(logn)
# Space Complexity ---> O(1)
