# Selection Sort Algorithm
def selectionSort(array):
  for i in range(0 , len(array)):
    min = i
    for j in range(i+1 , len(array)):
      # Compare the two elements
      if array[j] < array[min]:
        min = j
    # Swap the elements
    array[i] , array[min]  = array[min]  , array[i]
        
    
array = [2, 5 , 1 , 4 , 10 , 3]
selectionSort(array)
print(array)

# Time Complexity ---> O(n^2)
# Space Complexity ---> O(1)