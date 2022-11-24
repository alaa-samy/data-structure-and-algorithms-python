# Insertion Sort Algorithm
def insertion_sort(array):
  for i in range(1,len(array)):
    while i > 0 and array[i - 1] > array[i]:
      # Swap the two elements
      array[i-1] , array[i] = array[i] , array[i-1]
      i -= 1


array = [2, 5 , 1 , 4 , 10 , 3]
insertion_sort(array)
print(array)

# Time Complexity ---> O(n^2)
# Space Complexity ---> O(1)