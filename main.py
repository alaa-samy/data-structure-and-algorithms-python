# Bubble Sort Algorithm
def bubble_sort(array):
  for i in range(0, len(array)):
    for j in range(0 , len(array)-1):
      # Compare the two elements
      if array[j]> array[j+1]:
        # Swap the two elements
        temp = array[j]
        array[j] = array[j+1]
        array[j+1]=temp

array = [2 , 4 , 7 , 1 , 9 , 6]
bubble_sort(array)
print(array)