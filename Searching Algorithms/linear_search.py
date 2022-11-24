# Linear Search Algorithm
def linear_search(array , n):
  for i in range(0 , len(array)):
    if (array[i] == n):
      return i
  return -1


array = [2 , 5 , 1 , 7]
n = 4
result = linear_search(array , n)

if result == -1:
  print("Element not found")
else:
  print("Element is found at index ", result)

# Time Complexity ---> O(n)
# Space Complexity ---> O(1)