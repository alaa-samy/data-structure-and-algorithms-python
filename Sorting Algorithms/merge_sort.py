# Merge Sort Algorithm
def merge_sort(array):
  if len(array) > 1:
    m = len(array) // 2
    left = array[:m]
    right = array[m:]

    # Recursion
    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        array[k] = left[i]
        i += 1
      else:
        array[k] = right[j]
        j += 1
      k += 1

    while i < len(left):
      array[k] = left[i]
      i += 1
      k += 1

    while j < len(right):
      array[k] = right[j]
      j += 1
      k += 1


def print_array(array):
  for i in range(len(array)):
    print(array[i], end=' ')
  print()


if __name__ == '__main__':
  array = [6, 5, 12, 10, 9, 1]
  merge_sort(array)
  print_array(array)

# Time Complexity ---> O(n*logn)
# Space Complexity ---> O(n)
