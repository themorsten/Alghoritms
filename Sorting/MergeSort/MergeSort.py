def Merge(A,B):
  res = []
  i,j = 0,0
  Al = len(A)
  Bl = len(B)

  while(i < Al and j <Bl):
    if A[i]<B[j]:
      res.append(A[i])
      i+=1
    else:
      res.append(B[j])
      j+=1
  
  while i<Al:
    res.append(A[i])
    i+=1

  while j <Bl:
    res.append(B[j])
    j+=1

  return res


def MergeSort(A):
  if len(A) <= 1:
    return A
  mid = len(A)//2
  left = MergeSort(A[:mid])
  right = MergeSort(A[mid:])
  return Merge(left,right)



  ##################################################

  


A = [1,3,2,5,7,5,5,8,9,0]
MergeSort(A)
print(A)
