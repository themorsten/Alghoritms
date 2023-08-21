def BinarySearch(A, item):
  l = 0 
  r = len(A) - 1

  while l<=r:
    mid = (l+r)//2
    guess = A[mid]
    if guess == item:
      return mid

    if item < guess:
      r = mid -1
    else:
      l = mid +1
  
  return -1


#################################
A = [0, 1, 4, 7, 9, 11, 22, 25, 27, 30]
id = BinarySearch(A,27)
print(id)
